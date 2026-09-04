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

---

# ADR-007: Roll back Stream Sort through immutable versions instead of package backups

## Status

Accepted

## Date

2026-08-25

## Decision

Live Dispatcharr Stream Sort updates do not create a backup copy of the installed plugin directory. The directory contains reproducible package files and no changing plugin state; mutable Stream Sort data remains under `/data` outside the package directory.

Deployments still stage and validate the replacement package, preserve installed ownership, copy the package files, restart Dispatcharr, and inspect startup behavior. If rollback is needed, install a previously advertised immutable plugin version, which restores the package files from that version.

## Reason

An installed-directory backup duplicates files already recoverable through immutable registry version history. Version rollback is the simpler authoritative restoration path.

## Consequences

Stream Sort deployment procedures must use the registry's immutable versions for package rollback. Any future change that stores mutable state inside the plugin directory contradicts this decision and requires review before publication.

---

# ADR-008: Put FFmpeg Smart scan guidance in the registry description

## Status

Accepted

## Date

2026-08-26

## Decision

Use the FFmpeg Smart root and detail manifest `description` fields to state that new installations require a hardware capability scan, updates may require a capability recheck, and a required scan temporarily causes managed profiles to bypass FFmpeg Smart and hardware acceleration in favor of basic FFmpeg stream copy.

## Reason

Dispatcharr v0.29.0 displays the registry description in the managed plugin Details page before the Update action. Its manifest contract has no plugin-specific update-warning or release-note field, and its final install/update confirmation is generic core UI. The operator requested description placement rather than a Dispatcharr core change.

## Consequences

Root and detail descriptions must remain identical. The notice appears on the Details page and registry card surfaces that render the description; it does not appear as a custom block inside Dispatcharr's final confirmation modal. Future native warning-field support can supersede this placement after an official compatibility review.

## Provenance

- Dispatcharr v0.29.0 `PluginDetailPanel.jsx` and `PluginCard.jsx` review, 2026-08-26
- Operator wording correction: new installs require a scan; updates may require one

---

# ADR-009: Publish FFmpeg Smart adaptive probing only to the development channel

## Status

Accepted

## Date

2026-08-27

## Decision

Advance only the `dev` channel's FFmpeg Smart Profiles entry from completed stable `0.2.0` to immutable beta `0.2.1-beta.1` at source commit `d95aaf649b02e23dab76f19d274cb765b75bbca6`. Point the root entry back to the `dev` detail manifest, prepend beta.1, import the previously advertised stable `0.2.0` record from `main`, preserve older beta history, and leave the stable `main` channel unchanged.

Publish the tagged build for live Dispatcharr testing of canonical adaptive probing, manual probe-window migration, and profile-update browser-refresh guidance. Deployment authorization covers the development registry and live test instance only. It does not authorize a GitHub Release, distributable ZIP, stable registry update, or source-branch promotion.

## Reason

The wrapper and plugin beta tags are immutable, locally validated, and archive-verified. The user explicitly approved beta tagging and deployment so representative HDHomeRun sources and the deterministic CSPAN3 HE-AACv2 delayed-metadata edge can be validated through the actual managed profile path before broader publication.

## Consequences

Dispatcharr instances configured with the `dev` registry can discover and install `0.2.1-beta.1`. The root and detail manifests must agree on the exact tag, commit, URL, and minimum version while preserving stable `0.2.0`, beta.11, and older immutable history. Publication is complete only after registry validation, exact remote-head verification, repository refresh, installed-version verification, profile reconciliation, and live HDHomeRun/CSPAN3 checks.

## Provenance

- Operator decision Q&A and beta deployment approval, 2026-08-27
- Plugin tag: `v0.2.1-beta.1` at `d95aaf649b02e23dab76f19d274cb765b75bbca6`
- Canonical wrapper tag: `v1.1.1-beta.1` at `ecc64244dae2c0e80761da6f16be92d95b91d29a`

---

# ADR-010: Publish the modular FFmpeg Adaptive plugin beta only to dev

## Status

Accepted; supersedes ADR-009 only for the newest development-channel FFmpeg Smart build

## Date

2026-08-30

## Decision

Advance only the `dev` channel's FFmpeg Smart Profiles entry from `0.2.1-beta.1` to immutable `0.2.1-beta.2` at source commit `3c7b07cfe2d56540cd319179ef7c0d02318d2d38`. Prepend beta.2 to the existing version history, preserve every earlier immutable build, and leave the stable `main` channel and every unrelated plugin entry unchanged.

Publish the tagged build for managed Dispatcharr validation of the modular `ffmpeg-adaptive v0.1.0-beta.1` bundle, retired HDR/10-bit settings migration, automatic HDR/10-bit policy, explicit Force SDR/deinterlace behavior, hardware cache schema transition, and Stream/Output Profile execution. Deployment authorization covers the development registry and managed test instance only. It does not authorize a GitHub Release, stable source promotion, stable registry update, manual ZIP, Stream Sort change, or branch deletion.

## Reason

The source tag is immutable, its complete archive and seven-file runtime passed local and GitHub validation, and the canonical rewrite already passed comparative actual-stream coverage. The remaining risk is integration-specific: registry extraction must preserve the modular dependency, Dispatcharr must remove obsolete UI/saved values, and the managed launcher must rebuild its cache and run real Stream and `pipe:0` Output paths.

## Consequences

Dispatcharr instances configured with `dev` can discover and update to `0.2.1-beta.2`. The root and detail manifests must agree on the exact tag, commit, URL, and minimum version. Publication is complete only after registry validation, exact remote-head and public-manifest verification, managed update, installed module/license checks, profile reconciliation, zero-viewer cache rebuild, and representative live Stream/Output checks. Stable promotion remains a separate user decision.

The historical `v0.2.0` stable exception stays unchanged while `main` advertises that inherited-wrapper build. The new runtime's MIT license resolves the licensing gate only for later source versions; it does not retroactively alter historical registry metadata.

## Provenance

- Operator authorization in Codex on `2026-08-30`
- Plugin tag `v0.2.1-beta.2` at `3c7b07cfe2d56540cd319179ef7c0d02318d2d38`
- Canonical runtime `ffmpeg-adaptive v0.1.0-beta.1` at `80d648bbb0f93c45d5a7198bd7bf9260e9febd32`
- Plugin workflow `33320334916` and clean extracted-archive validation
- Development registry commit `d6495c932cd53248ac1128b18ebe7a872d1f20f1`
  and workflow `33320510384`
- Managed repository 37 update, installed source/license verification,
  profile migration/reconciliation, schema-2 cache rebuild, and actual
  1080p/1080i/720p Stream plus `pipe:0` Output Profile validation on
  `2026-08-30`

---

# ADR-011: Replace the development FFmpeg Smart beta with the corrective fidelity build

## Status

Accepted; supersedes ADR-010 only for the newest development-channel FFmpeg Smart build

## Date

2026-08-30

## Decision

Advance only the `dev` channel's FFmpeg Smart Profiles entry from
`0.2.1-beta.2` to immutable corrective beta `0.2.1-beta.3` at source commit
`dd54d4cc82a454135c4eb3b75eeeb5eb48713fe6`. Prepend beta.3 to the existing
version history, retain beta.2 and every earlier immutable build, and leave
stable `main` plus every unrelated plugin entry unchanged.

Publish the tagged build for managed validation of
`ffmpeg-adaptive v0.1.0-beta.2`: the cache policy must become stale, the
operator must rebuild with zero viewers, and representative 1080p, 1080i,
720p, finite `pipe:0`, and overlapping multi-GPU paths must pass. Deployment
authorization covers the development registry and managed test instance only.
It does not authorize a GitHub Release, manual ZIP, stable source promotion,
stable registry update, Stream Sort change, or branch deletion.

## Reason

Canonical wrapper comparison proved that beta.1's capacity benchmark did not
match runtime hardware decode and could under-report capabilities. The
corrective beta uses the same hardware path for benchmark and runtime, applies
the measured per-device low-power policy, ties capacity to the measured
accelerator/codec pair, and gives upper-bound scans a deadline. The plugin's
workflow and exact tag archive pass, so the remaining risk is the managed
update, stale-cache transition, and live installed behavior.

## Consequences

Dispatcharr instances configured with `dev` can discover and update to
`0.2.1-beta.3`. The root and detail manifests must agree on the exact tag,
commit, URL, and minimum version while preserving the full history. Managed
starts use the existing degraded stream-copy path until the fresh hardware
rebuild succeeds. Publication is complete only after registry validation,
exact remote and public-manifest verification, managed repository 37 update,
installed source/license checks, cache rebuild, actual-stream and scheduler
checks, and final viewer/process cleanup.

## Provenance

- Operator authorization in Codex on `2026-08-30`
- Plugin tag `v0.2.1-beta.3` at
  `dd54d4cc82a454135c4eb3b75eeeb5eb48713fe6`
- Canonical runtime `ffmpeg-adaptive v0.1.0-beta.2` at
  `4df6c12e395187fc0080f858685a3c6ebd7a8c42`
- Plugin workflow `33333007420` and clean extracted-tag archive validation
- Development-registry commit
  `50489521b1b6350bc95f300ceaf77a8bb7c372da` and workflow `33333093699`
- Managed repository 37 beta.2-to-beta.3 update, exact installed runtime and
  MIT notice, idempotent profiles, valid VAAPI/HEVC 18/14 cache with confirmed
  rejection at 19/15, decoded-frame actual-stream matrix, overlapping both-GPU
  scheduler pass, cleanup, and final process audit on `2026-08-30`

---

# ADR-012: Publish the Lineuparr excluded-aliases beta only to dev

## Status

Accepted

## Date

2026-09-04

## Decision

Add Lineuparr `1.26.2471558-beta.1` only to the `dev` registry. Advertise immutable source tag `v1.26.2471558-beta.1`, which dereferences to the validated fork `dev` composition at `f03ea7e1746e48640c94028758ba3325d0ceef62`. Create a development per-plugin manifest, preserve every unrelated root entry, and leave registry `main` unchanged.

The source composition is current upstream `main` plus the isolated `feature/excluded-aliases` implementation and a separate fork-only beta metadata branch. Publication does not authorize a fork GitHub Release, stable registry entry, managed Dispatcharr refresh, installation, or deployment.

## Reason

The operator wants to test denied M3U matches through the managed plugin workflow before proposing the Lineuparr schema and matcher change upstream. The immutable beta tag makes that exact composition reproducible, and the incremented synchronized version lets Dispatcharr distinguish it from upstream `1.26.2421451`.

## Consequences

- Development users can discover the beta from `matrix2669 Plugins (dev)`.
- Root and detail manifests identify the exact tag, commit, version, archive, author, license, icon, and upstream minimum Dispatcharr version.
- Upstream remains the stable Lineuparr source; the plugin stays absent from registry `main`.
- A correction requires a new immutable beta version and tag; the existing tag and metadata must never move.
- Managed installation and behavior validation remain separate, explicitly authorized work.

## Provenance

- Operator authorization dated `2026-09-04`: add the composed Lineuparr excluded-aliases build to the Dispatcharr development manifest
- Source tag: `v1.26.2471558-beta.1`
- Source commit: `f03ea7e1746e48640c94028758ba3325d0ceef62`
