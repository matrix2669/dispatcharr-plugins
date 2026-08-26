# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-25.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `feature/ffmpeg-smart-v0.2.0-beta.3` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.3` test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.4` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.4` scoped-options test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.5` | feature | active | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.5` inherited-default guidance build. |
| `fix/stream-sort-v0.3.6-beta.4` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.4` correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.6` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.6` cancellation and analyzer-serialization correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.9` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.9` combined-capture correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.10` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.10` telemetry-integrity correction only to the tagged-build channel. |
| `feature/stream-sort-v0.3.6-beta.11` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.11` adaptive analysis policies only to the tagged-build channel. |

## Branch Records

### `main`

- Type: long-lived
- Status: active
- Purpose: released Dispatcharr registry for plugins with explicitly approved GitHub Releases
- Required publication evidence: user approval, stable source tag, normal GitHub Release, exact source commit, validated install archive, and successful Dispatcharr installation
- Exclusions: beta tags, completed-but-unreleased versions, moving source branches, and unrelated `dev` entries
- Promotion rule: make a focused change from `main`; never merge the complete `dev` catalog into this branch
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/main/manifest.json`

### `fix/stream-sort-v0.3.6-beta.4`

- Purpose: publish the reviewed Stream Sort scheduler, TTL, telemetry, and reporting corrections as immutable beta `0.3.6-beta.4`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, and any moving source branch URL
- Completion: validate the full development registry, merge into `dev`, publish `dev`, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.6`

- Purpose: publish the reviewed Stream Sort analyzer-serialization, safe-stop, checkpointing, and provisional-dead retry corrections as immutable beta `0.3.6-beta.6`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, branch ledger, and pending standards-reconciliation records
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to viewer-aware provider capacity
- Source evidence: immutable tag `v0.3.6-beta.6` resolves to `ab9dfd3c28afe61f757cfb6a40cd0217760f09f3`; the downloaded archive preserves `stream_sorter/plugin.json`, compiles, and passes all 107 source tests
- Completion: validate the full development registry, merge into `dev`, publish `dev`, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.9`

- Purpose: publish the reviewed Stream Sort combined-capture retry, completion-accounting, and first-baseline reason corrections as immutable beta `0.3.6-beta.9`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branches, provider-specific scheduling, and report compaction
- Source evidence: immutable tag `v0.3.6-beta.9` resolves to `9eea52417c1f2f25307f9d52825bd41a22fb2bb7`; the downloaded archive preserves `stream_sorter/plugin.json`, reports the synchronized beta.9 version, compiles, and passes all 129 source tests
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm managed installation, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.10`

- Purpose: publish the reviewed Stream Sort scan-boundary transition and throughput-accounting corrections as immutable beta `0.3.6-beta.10`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to Dispatcharr compatibility metadata
- Source evidence: immutable tag `v0.3.6-beta.10` resolves to `3f62cdeb50bb41ad1d02eec3f05d5fffaad55c44`; the source passed 131 tests, Python compilation, version consistency, diff checks, and workspace standards reconciliation
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm Dispatcharr installs beta.10, and remove this record only after the short-lived remote branch is deleted

### `feature/stream-sort-v0.3.6-beta.11`

- Purpose: publish the reviewed Stream Sort rolling media history, minimum-bitrate retry floor, placeholder segmentation, adaptive dead TTL, and shared freshness policies as immutable beta `0.3.6-beta.11`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, deployment decision, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to Dispatcharr compatibility metadata
- Source evidence: immutable tag `v0.3.6-beta.11` resolves to `3097708e9db5621db76ef8f6238e20a2e0498234`; the archive preserves `stream_sorter/plugin.json`, reports synchronized beta.11, and the source passes 138 tests, Python compilation, manifest parsing, diff checks, and workspace standards reconciliation
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm Dispatcharr installs beta.11, and remove this record only after the short-lived remote branch is deleted

### `dev`

- Type: long-lived
- Status: active
- Purpose: continuous tagged-build registry containing the newest approved immutable tag for every retained plugin
- Origin: created from the complete legacy `dev-test` history, then reconciled with stable entries that were added to `main` after the histories diverged
- Versions: beta tags during active testing; completed stable tags after feature or fix completion, whether released or not
- Stable reuse: when the newest tagged version is identical to `main`, the root index reuses the unchanged `main` per-plugin manifest
- Exclusions: moving source branches, untagged builds, and implicit promotion to `main`
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/dev/manifest.json`
- Current Arr Stack build: released stable version `0.2.0`, reusing the matching `main` detail manifest; beta `0.2.0-beta.1` metadata remains unindexed for history
- Validation: the development validator and all registry tests pass; the stable tag resolves to source commit `2c7441bd4cceb8e2a68b50a0c24b064e87c6eb46`
- Current Mustarrd DVR build: beta `0.2.13-beta.2` from source repository `matrix2669/Dispatcharr-Mustarrd-DVR-Plugin`; plugin name and slug remain unchanged
- Mustarrd DVR validation: source tag resolves to `606d2c23775004581c22213b0b1c7ac59e00b4d6`; the GitHub tag archive preserves `mustarrd-dvr-handoff/`; the immutable icon URL is a 1254×1254 PNG; the development validator and all registry tests pass
- Current FFmpeg Smart build: beta `0.2.0-beta.4` from source commit `08ce3c5ab13f36a22b03826b4d3a847d39a339b3`; the immutable tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files. The plugin passed 25 source tests, canonical wrapper validation, remote immutable-source verification, repeated synchronization, and archive inspection; the development registry validator and all registry tests pass. Prior beta.2 live state-persistence, recache, restart, and `pipe:0` evidence remains the latest installed-runtime baseline until beta.4 deployment validation.
- Current Stream Sort build: beta `0.3.6-beta.11` from source commit `3097708e9db5621db76ef8f6238e20a2e0498234`; the immutable tag archive preserves `stream_sorter/plugin.json`, reports the synchronized beta.11 version, compiles, and passes all 138 source tests. Rolling direct-probe media history suppresses one-scan noise, low-bitrate and placeholder outcomes receive explicit retry/report treatment, dead checks use adaptive exact TTLs, and sorting shares analysis freshness settings.

### `feature/ffmpeg-smart-v0.2.0-beta.3`

- Type: short-lived feature branch
- Status: merged into `dev` at `660297e` and published through `dev` at `b005781`; remote raw-manifest and GitHub validation checks pass
- Base: `dev` at `739937b`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.2` to the approved immutable `0.2.0-beta.3` tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.3` resolves to commit `59f1c207cf68f9b6e8ca289df6b9188d2b5b2565`; the tag archive contains the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, or runtime code.
- Validation: exact tag resolution and archive layout, dev registry validator, all five registry unit tests, JSON parsing, `git diff --check`, and complete-diff review pass; only FFmpeg Smart metadata, history, changelog, and this ledger change.

### `feature/ffmpeg-smart-v0.2.0-beta.4`

- Type: short-lived feature branch
- Status: merged into `dev` at `1d36df9` and published through `dev` at `877ef8b`; remote raw manifests and GitHub validation pass
- Base: `dev` at `942144b`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.3` to the approved immutable `v0.2.0-beta.4` scoped-options tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.4` resolves to commit `08ce3c5ab13f36a22b03826b4d3a847d39a339b3`; the reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, or runtime code.
- Validation: exact plugin tag resolution and archive layout, development registry validator, all five registry unit tests, JSON parsing, prior-version retention, `git diff --check`, and complete-diff review pass; only FFmpeg Smart metadata, history, changelog, and this ledger changed.
- Completion: `dev` advertises immutable beta.4 from exact source commit `08ce3c5`; the raw root/detail manifests agree, prior immutable versions remain indexed, and the published manifest workflow completed successfully.

### `feature/ffmpeg-smart-v0.2.0-beta.5`

- Type: short-lived feature branch
- Status: active
- Base: `dev` at `442a2de`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.4` to the approved immutable `v0.2.0-beta.5` inherited-default guidance tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.5` resolves to commit `6fb786ddc01105d3328a49be4224b2e4d759e485`; the reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and branch-ledger corrections only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, or runtime code.
- Validation plan: exact plugin tag resolution and archive layout, development registry validator, all registry unit tests, JSON parsing, prior-version retention, `git diff --check`, and complete-diff review.
