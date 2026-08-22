# Registry Publication Process

This repository publishes branch-backed Dispatcharr registry channels. It does not publish GitHub Releases or a repository version.

- `main` is the released channel.
- `dev` is the continuous tagged-build channel.

Each registry entry points to an immutable build in a separate plugin source repository.

## Common validation

Before changing either channel:

1. Refresh the registry and plugin source repositories.
2. If the supported, minimum, tested, or deployed Dispatcharr version changed, refresh the official Dispatcharr repository and revalidate its current plugin manifest, archive, layout, version comparison, and installation/update requirements. Record the reviewed Dispatcharr version or tag, exact commit, repository URL, and date.
3. Confirm the source tag and full commit SHA.
4. Inspect the exact archive URL that Dispatcharr will install.
5. Confirm the archive contains the plugin at the layout expected by the reviewed Dispatcharr revision.
6. Preserve all unrelated root entries and prior per-plugin version history.
7. Update the root and per-plugin manifests together.
8. Run `python3 scripts/validate_registry.py --channel <main|dev>`.
9. Run `python3 -m unittest discover -s tests -v`.
10. Review the complete diff for unintended plugin additions, removals, URL changes, or version-history rewrites.

If a Dispatcharr version changed and the matching current repository requirements cannot be verified, stop. Do not publish using cached assumptions.

Never move an advertised tag, replace an artifact for an existing version, or point `latest_url` at a moving branch.

## Tagged-build publication on `dev`

1. Start a focused change from the current `dev` branch.
2. Verify that the plugin tag exists on the intended source-repository commit.
3. Choose the newest approved tag: `MAJOR.MINOR.PATCH-beta.N` during active testing or `MAJOR.MINOR.PATCH` after feature or fix work is complete.
4. Add or update the plugin only in the `dev` manifests.
5. Keep the root registry identity on `matrix2669 Plugins (dev)` and `tree/dev`.
6. If the newest tag differs from `main`, use a `/dev/` per-plugin manifest containing that exact tag. If it is the same released version already advertised by `main`, reuse the `/main/` per-plugin manifest instead of duplicating a no-op detail update.
7. Push the focused registry change.
8. Refresh the tagged-build repository in Dispatcharr and confirm it detects the version increment.
9. Install or update the plugin and verify the installed version and required behavior.

When a beta cycle ends, move the entry to the completed stable tag. Do not remove the plugin from `dev`, switch it to a moving source branch, or require a GitHub Release. If no newer beta exists, leave the entry on the newest completed stable tag.

A completed stable tag in `dev` does not authorize a `main` change.

## Release publication on `main`

1. Start a focused change from the current `main` branch; do not merge the complete `dev` channel.
2. Obtain explicit user approval to release the completed stable plugin version.
3. Verify the normal Semantic Version tag, GitHub Release, attached manual-install artifact when required, checksum when provided, and exact source commit.
4. Confirm the tested stable archive matches the release metadata.
5. Add or update only that plugin in the `main` manifests.
6. Use `matrix2669 Plugins`, the repository root URL, and `/main/` raw manifest URLs.
7. Push the focused released-channel change.
8. Refresh the `main` repository in Dispatcharr and test installation or update from that channel.

The existence of a tag is insufficient. If the GitHub Release or explicit approval is missing, stop and keep the plugin absent from `main`.

## `dev-test` to `dev` migration

1. Refresh all remote refs and record the current `dev-test` head.
2. Create `dev` from that exact head so testing history is preserved.
3. Change the testing registry name, registry URL, and every raw per-plugin manifest URL to `dev`.
4. Validate the complete `dev` manifest and publish the branch.
5. Update configured Dispatcharr testing repository URLs from `/dev-test/manifest.json` to `/dev/manifest.json`.
6. Refresh the repository and confirm all expected plugins and versions remain available.
7. Verify at least one installed testing plugin still resolves to the exact advertised build.
8. Search the workspace and related repositories for remaining active `dispatcharr-plugins:dev-test` dependencies.
9. Delete the legacy branch only after those checks pass, then update `BRANCHES.md` to remove it and list `dev` as active.
