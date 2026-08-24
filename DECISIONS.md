# DECISIONS.md

This file records significant architecture and workflow decisions for the matrix2669 Dispatcharr plugin registry.

---

# ADR-001: Keep plugin code and release ownership in source repositories

## Status

Accepted

## Date

2026-08-11

## Decision

This repository contains only Dispatcharr registry indexes and per-plugin publication metadata. Each plugin source repository owns runtime code, tests, tags, GitHub Releases, installable artifacts, and release history.

## Reason

Plugins evolve independently and need separate validation and version histories. The registry should answer only which immutable build a channel installs.

## Consequences

Do not copy plugin code or build output here. Registry changes must be reconciled with the authoritative source tag, commit, release state, and archive layout.

## Provenance

- Registry initialization: `f2c0b25`
- Original repository README

---

# ADR-002: Use `main` and `dev` as release and tagged-build registry channels

## Status

Accepted

## Date

2026-08-22

## Decision

`main` is the released Dispatcharr registry and `dev` is the continuous tagged-build registry. The legacy `dev-test` branch is replaced by `dev` after a controlled migration.

For every plugin retained in the channel, `dev` advertises its newest approved immutable tag. That may be a beta during active testing or a completed stable Semantic Version after feature or fix work finishes. A completed stable version does not require a GitHub Release and remains distinct from a released version in `main`.

If that newest tag is already the exact released version in `main`, the `dev` root index reuses the `main` per-plugin manifest. If `dev` advertises a different beta or completed-but-unreleased stable tag, it references a `dev` per-plugin manifest instead.

This follows the workspace's supported standalone metadata-registry profile: the branches are deployed registry channels, not plugin source integration branches. Short-lived work branches start from and return to only the channel they modify. Testing metadata is never promoted by merging the complete `dev` branch into `main`.

## Reason

The channel names should align with the standalone repository model while retaining a clear tagged/released split. Keeping each plugin on its newest tag avoids needless manifest removal or fallback changes between beta cycles. Reusing an identical `main` detail manifest avoids duplicate edits when no newer tag exists. A focused release publication prevents unrelated tagged but unreleased entries from leaking into `main`.

## Consequences

The `dev` branch begins from the exact legacy testing history. All testing manifest URLs and configured Dispatcharr repository URLs change from `dev-test` to `dev`. The legacy branch is deleted only after consumer verification.

## Provenance

- Legacy testing head: `1089ad8fc2b388931cc3dc5466b8674c03e9e171`
- User direction on 2026-08-22: rename the registry testing branch from `dev-test` to `dev`

---

# ADR-003: Separate completed stable versions from released versions

## Status

Accepted

## Date

2026-08-22

## Decision

Plugin tags are advertised through this repository's `dev` channel. Beta tags identify active test builds; normal Semantic Version tags identify completed feature or fix work. Neither kind of tag requires a GitHub Release.

A plugin is added to `main` only after the user explicitly approves and publishes a GitHub Release for a completed stable tag in its source repository.

A tag—prerelease-looking or otherwise—does not by itself declare stable readiness.

## Reason

Dispatcharr needs version increments to test updates, and the tagged-build channel should remain useful between beta cycles. A GitHub Release and `main` entry communicate the separate decision that a completed stable version is generally available and ready for release distribution.

## Consequences

Unreleased plugins may advance through beta and completed stable tags while remaining absent from `main`. `dev` keeps the newest approved tag for each retained plugin. Corrections use new versions; advertised tags and artifacts are never replaced.

## Provenance

- Workspace ADR-010
- Stream Sort `v0.3.6-beta.2` testing publication

---

# ADR-004: Keep the registry repository unversioned

## Status

Accepted

## Date

2026-08-22

## Decision

This repository has no `VERSION`, release tags, or GitHub Releases of its own. Channel branch commits publish independently versioned plugin metadata.

## Reason

A single registry version would compete with the authoritative version of every plugin entry without improving Dispatcharr's update behavior.

## Consequences

`RELEASE.md` describes channel publication rather than a repository release. Git history and `CHANGELOG.md` record registry changes, while plugin changelogs record plugin behavior.

---

# ADR-005: Require immutable and internally consistent manifest metadata

## Status

Accepted

## Date

2026-08-22

## Decision

Every advertised build uses an immutable semantic tag or full commit SHA. Root and per-plugin manifests must agree on identity, current version, minimum Dispatcharr version, source repository, and archive URL. Version history retains prior advertised builds and identifies the exact source commit.

Per-plugin metadata may remain in the tree after its root entry is removed. Such an unindexed manifest is archival and is not advertised to Dispatcharr.

## Reason

Moving references make installations irreproducible, and duplicated inconsistent fields can cause Dispatcharr to display or install a different build than intended.

## Consequences

Automated validation runs for both channels. Stable release approval and upstream artifact existence remain manual verification gates because structural validation cannot infer intent or readiness.

---

# ADR-006: Refresh Dispatcharr manifest requirements on every version change

## Status

Accepted

## Date

2026-08-22

## Decision

Whenever the supported, minimum, tested, or deployed Dispatcharr version changes, registry publication requires a fresh review of the matching official Dispatcharr repository revision. The review records the Dispatcharr version or tag, exact commit, repository URL, and date, then revalidates manifest fields, version comparison, archive handling, plugin layout, minimum-version behavior, and installation/update behavior.

A change to `min_dispatcharr_version` or an upgrade of the Dispatcharr validation instance triggers this gate.

## Reason

Dispatcharr owns the consumer-side plugin contract. Registry validation can become stale when Dispatcharr changes its schema, loader, extraction rules, or update behavior.

## Consequences

Agents must update repository validation and documentation when the Dispatcharr contract changes and perform an installation or update check on the new version. Publication is blocked when the matching current Dispatcharr requirements cannot be verified; cached requirements are not sufficient evidence.
