#!/usr/bin/env python3
"""Validate a matrix2669 Dispatcharr registry channel."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-beta\.(0|[1-9]\d*))?$")
SHA = re.compile(r"^[0-9a-f]{40}$")
IMMUTABLE_REF = re.compile(r"^(?:v\d+\.\d+\.\d+(?:-beta\.\d+)?|[0-9a-f]{40})$")
REQUIRED_PLUGIN_FIELDS = (
    "slug",
    "name",
    "description",
    "author",
    "license",
    "repo_url",
    "latest_version",
)


class ValidationError(Exception):
    pass


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{path}: cannot load JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"{path}: top-level value must be an object")
    return value


def require_fields(value: dict, fields: tuple[str, ...], context: str) -> None:
    missing = [field for field in fields if not value.get(field)]
    if missing:
        raise ValidationError(f"{context}: missing required fields: {', '.join(missing)}")


def archive_ref(url: str, context: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "api.github.com":
        raise ValidationError(f"{context}: archive URL must use https://api.github.com")
    marker = "/zipball/"
    if marker not in parsed.path:
        raise ValidationError(f"{context}: archive URL must contain /zipball/<immutable-ref>")
    ref = parsed.path.split(marker, 1)[1]
    if not IMMUTABLE_REF.fullmatch(ref):
        raise ValidationError(f"{context}: archive reference is not an immutable tag or full commit SHA: {ref}")
    return ref


def validate_version(version: str, channel: str, context: str) -> None:
    match = SEMVER.fullmatch(version)
    if not match:
        raise ValidationError(f"{context}: unsupported version {version!r}")
    if channel == "main" and match.group(4) is not None:
        raise ValidationError(f"{context}: stable channel cannot advertise beta version {version!r}")


def requires_local_detail_validation(channel: str, detail_channel: str) -> bool:
    """Return whether the referenced detail manifest belongs to this checkout."""
    return not (channel == "dev" and detail_channel == "main")


def validate_channel(root: Path, channel: str) -> None:
    expected_name = "matrix2669 Plugins" if channel == "main" else "matrix2669 Plugins (dev)"
    expected_registry_url = (
        "https://github.com/matrix2669/dispatcharr-plugins"
        if channel == "main"
        else "https://github.com/matrix2669/dispatcharr-plugins/tree/dev"
    )
    manifest_prefix = "/matrix2669/dispatcharr-plugins/"

    registry = load_json(root / "manifest.json")
    if registry.get("registry_name") != expected_name:
        raise ValidationError(f"manifest.json: registry_name must be {expected_name!r}")
    if registry.get("registry_url") != expected_registry_url:
        raise ValidationError(f"manifest.json: registry_url must be {expected_registry_url!r}")

    plugins = registry.get("plugins")
    if not isinstance(plugins, list):
        raise ValidationError("manifest.json: plugins must be an array")

    seen_slugs: set[str] = set()
    for index, summary in enumerate(plugins):
        context = f"manifest.json plugins[{index}]"
        if not isinstance(summary, dict):
            raise ValidationError(f"{context}: value must be an object")
        require_fields(summary, REQUIRED_PLUGIN_FIELDS + ("manifest_url", "latest_url", "min_dispatcharr_version"), context)

        slug = summary["slug"]
        if slug in seen_slugs:
            raise ValidationError(f"{context}: duplicate slug {slug!r}")
        seen_slugs.add(slug)
        validate_version(summary["latest_version"], channel, context)
        archive_ref(summary["latest_url"], f"{context} latest_url")
        manifest_url = summary["manifest_url"]
        if f"{manifest_prefix}main/plugins/" in manifest_url:
            detail_channel = "main"
        elif f"{manifest_prefix}dev/plugins/" in manifest_url:
            detail_channel = "dev"
        else:
            raise ValidationError(f"{context}: manifest_url must reference the main or dev channel")
        if channel == "main" and detail_channel != "main":
            raise ValidationError(f"{context}: main entries must reference main per-plugin manifests")
        if detail_channel == "main" and "-beta." in summary["latest_version"]:
            raise ValidationError(f"{context}: beta versions cannot reuse a main per-plugin manifest")

        path_match = re.search(r"/plugins/([^/]+)/manifest\.json$", urlparse(manifest_url).path)
        if not path_match:
            raise ValidationError(f"{context}: manifest_url must end with /plugins/<directory>/manifest.json")

        # A dev entry may deliberately reuse an unchanged main detail manifest.
        # The main channel validates that file; the historical local dev copy is
        # unindexed and must not be mistaken for the referenced main document.
        if not requires_local_detail_validation(channel, detail_channel):
            continue

        detail_path = root / "plugins" / path_match.group(1) / "manifest.json"
        if not detail_path.is_file():
            raise ValidationError(f"{context}: missing {detail_path.relative_to(root)}")
        detail = load_json(detail_path)
        detail_context = str(detail_path.relative_to(root))
        require_fields(detail, REQUIRED_PLUGIN_FIELDS + ("registry_name", "registry_url", "latest", "versions"), detail_context)

        for field in REQUIRED_PLUGIN_FIELDS:
            if detail.get(field) != summary.get(field):
                raise ValidationError(f"{detail_context}: {field} does not match root manifest")
        detail_expected_name = "matrix2669 Plugins" if detail_channel == "main" else "matrix2669 Plugins (dev)"
        detail_expected_url = (
            "https://github.com/matrix2669/dispatcharr-plugins"
            if detail_channel == "main"
            else "https://github.com/matrix2669/dispatcharr-plugins/tree/dev"
        )
        if detail["registry_name"] != detail_expected_name or detail["registry_url"] != detail_expected_url:
            raise ValidationError(f"{detail_context}: registry identity does not match its {detail_channel} manifest URL")

        latest = detail["latest"]
        versions = detail["versions"]
        if not isinstance(latest, dict) or not isinstance(versions, list) or not versions:
            raise ValidationError(f"{detail_context}: latest must be an object and versions must be non-empty")
        if latest.get("version") != detail["latest_version"] or versions[0].get("version") != detail["latest_version"]:
            raise ValidationError(f"{detail_context}: latest_version, latest.version, and versions[0].version must agree")
        if latest.get("url") != summary["latest_url"] or latest.get("latest_url") != summary["latest_url"]:
            raise ValidationError(f"{detail_context}: latest archive URL does not match root manifest")
        if latest.get("min_dispatcharr_version") != summary["min_dispatcharr_version"]:
            raise ValidationError(f"{detail_context}: minimum Dispatcharr version does not match root manifest")

        seen_versions: set[str] = set()
        for version_index, item in enumerate(versions):
            item_context = f"{detail_context} versions[{version_index}]"
            if not isinstance(item, dict):
                raise ValidationError(f"{item_context}: value must be an object")
            require_fields(item, ("version", "url", "commit_sha", "commit_sha_short", "build_timestamp", "min_dispatcharr_version"), item_context)
            validate_version(item["version"], channel, item_context)
            if item["version"] in seen_versions:
                raise ValidationError(f"{item_context}: duplicate version {item['version']!r}")
            seen_versions.add(item["version"])
            ref = archive_ref(item["url"], f"{item_context} url")
            if not SHA.fullmatch(item["commit_sha"]):
                raise ValidationError(f"{item_context}: commit_sha must be 40 lowercase hexadecimal characters")
            if item["commit_sha_short"] != item["commit_sha"][:7]:
                raise ValidationError(f"{item_context}: commit_sha_short must be the first seven SHA characters")
            if ref.startswith("v") and ref[1:] != item["version"]:
                raise ValidationError(f"{item_context}: tag archive {ref!r} does not match version")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", item["build_timestamp"]):
                raise ValidationError(f"{item_context}: build_timestamp must be UTC ISO-8601 with Z suffix")

        for field in ("version", "url", "commit_sha", "commit_sha_short", "build_timestamp", "min_dispatcharr_version"):
            if latest.get(field) != versions[0].get(field):
                raise ValidationError(f"{detail_context}: latest.{field} must match versions[0].{field}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", choices=("main", "dev"), required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate_channel(args.root.resolve(), args.channel)
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {args.channel} registry at {args.root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
