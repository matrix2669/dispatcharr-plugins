# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-26.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `feature/ffmpeg-smart-v0.2.0-beta.3` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.3` test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.4` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.4` scoped-options test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.5` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.5` inherited-default guidance build. |
| `feature/ffmpeg-smart-v0.2.0-beta.6` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.6` launcher and cache-maintenance correction. |
| `feature/ffmpeg-smart-update-disclaimer` | feature | merged | `dev` | `dev` | Advertise FFmpeg Smart Profiles `v0.2.0-beta.7` with degraded stream-copy fallback and install-versus-update scan guidance. |
| `fix/ffmpeg-smart-v0.2.0-beta.8` | fix | merged | `dev` | `dev` | Replace beta.7 with the immutable corrective beta.8 canonical-wrapper repin. |
| `fix/ffmpeg-smart-v0.2.0-beta.9` | fix | active | `dev` | `dev` | Restore persistent degraded notification-center reactivation after dismissal. |
| `fix/stream-sort-v0.3.6-beta.4` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.4` correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.6` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.6` cancellation and analyzer-serialization correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.9` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.9` combined-capture correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.10` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.10` telemetry-integrity correction only to the tagged-build channel. |
| `feature/stream-sort-v0.3.6-beta.11` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.11` adaptive analysis policies only to the tagged-build channel. |

## Branch Records

### `feature/ffmpeg-smart-update-disclaimer`

- Type: short-lived feature branch
- Status: merged into `dev` at `4b9d4a5` and published through `dev` at `f885da0`; remote raw manifests and GitHub validation pass
- Base: `dev` at `eab2f93f7c9af0daf425ed17b324e7ddb7d75dc6`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.6` to approved immutable `v0.2.0-beta.7`, while showing that new installations require a hardware capability scan, updates may require a recheck, and managed profiles fall back to basic stream copy until a required scan succeeds.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.7` resolves to commit `600ba14572ab48f4d920c2cfd7ad4ac9fffce787`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, and synchronized beta.7 plugin metadata.
- Scope: FFmpeg Smart root/detail metadata and descriptions, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Related work: `Dispatcharr-FFmpeg-Smart-Plugin` branch `feature/degraded-proxy-fallback`.
- Validation: exact tag resolution and archive layout, synchronized beta.7 plugin metadata, 37 plugin tests, canonical-wrapper validation, remote immutable-source verification, root/detail description agreement, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, complete-diff review, published raw-manifest agreement, and GitHub workflow run `33014922697` pass.
- Completion: `dev` advertises immutable beta.7 from exact source commit `600ba14`; beta.6 through v0.1.0 remain indexed, and no `main` or unrelated plugin metadata changed. Installed-update validation remains pending.

### `fix/ffmpeg-smart-v0.2.0-beta.8`

- Type: short-lived corrective branch
- Status: merged into `dev` at `be35192` and published through `dev` at `2f35359`; remote raw manifests and GitHub validation pass
- Base: `dev` at `e92fc6c` after beta.7 registry publication and evidence recording.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.7` to corrective immutable `v0.2.0-beta.8`, preserving fallback behavior while repinning to green canonical `ffmpeg-asr v1.1.0-beta.6`.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.8` resolves to commit `5309b16ae2440f36238fa5a5426cf2e2ecc9f918`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, synchronized beta.8 metadata, and canonical source commit `aeff09204000f58aa6fdd3a14781935f77a0823a`.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: exact tag/archive/source-pin inspection, 37 plugin tests, plugin and canonical GitHub workflows, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, complete-diff review, published raw-manifest agreement, and registry workflow run `33016050222` pass.
- Completion: `dev` advertises immutable beta.8 from exact source commit `5309b16`; beta.7 through v0.1.0 remain indexed, the install/update scan disclaimer is unchanged, and no `main` or unrelated plugin metadata changed. Installed-update validation remains pending.

### `fix/ffmpeg-smart-v0.2.0-beta.9`

- Type: short-lived corrective branch
- Status: active
- Base: `dev` at `d3c1271` after beta.8 registry publication and evidence recording.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.8` to corrective immutable `v0.2.0-beta.9`, making every new fallback invocation restore a dismissed notification-center entry immediately instead of producing only a toast.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.9` resolves to commit `d25b44b8999dba3aaeb82e264fb75335bbcacc88`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, synchronized beta.9 metadata, and the explicit `is_dismissed: false` WebSocket payload.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, canonical wrapper, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: official Dispatcharr v0.29.0 notification-contract review, exact tag/archive inspection, 37 plugin tests, source workflow runs, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, and complete-diff review pass. Published raw manifests, registry workflow, and installed beta.9 reactivation remain pending.

### `main`

- Type: long-lived
- Status: merged into `dev` at `af9af1f` and published through `dev` at `36c2e20`; remote raw manifests and GitHub validation pass
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
- Current FFmpeg Smart build: corrective beta `0.2.0-beta.8` from source commit `5309b16ae2440f36238fa5a5426cf2e2ecc9f918`; the immutable tag archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, and canonical `ffmpeg-asr v1.1.0-beta.6` pin. The plugin passed 37 source tests covering degraded stream-copy fallback, notification re-display after every invocation, launcher behavior, cache status, profile generation, and restart semantics; canonical-wrapper validation, source and tag GitHub workflows, archive inspection, the development registry validator, and all registry tests pass.
- Current Stream Sort build: beta `0.3.6-beta.12` from source commit `9bec63a1d72082e1efffa42bd0c758dcf3bf29dd`; the immutable tag archive preserves `stream_sorter/plugin.json`, reports the synchronized beta.12 version, compiles, and passes all 151 source tests. Known placeholder confirmations now avoid redundant retries and downstream probes, legacy per-run caps are ignored, automatic reliability collection is explicit, and completion logs include runtime plus the authoritative placeholder/other-dead breakdown.

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
- Status: merged into `dev` at `a3ae423` and published through `dev` at `73d4fbd`; installed-update validation remains pending
- Base: `dev` at `442a2de`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.4` to the approved immutable `v0.2.0-beta.5` inherited-default guidance tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.5` resolves to commit `6fb786ddc01105d3328a49be4224b2e4d759e485`; the reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and branch-ledger corrections only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, or runtime code.
- Validation: exact remote tag resolution to `6fb786d`, downloaded archive layout and beta.5 plugin metadata, development registry validator, all five registry unit tests, JSON parsing, prior-version retention, `git diff --check`, and complete-diff review pass; unrelated plugin entries remain unchanged.
- Completion: `dev` advertises immutable beta.5 from exact source commit `6fb786d`; the raw root/detail manifests agree, beta.4 through v0.1.0 remain indexed, and the published manifest workflow completed successfully.

### `feature/ffmpeg-smart-v0.2.0-beta.6`

- Type: short-lived feature branch
- Status: merged into `dev` at `a3ae423` and published through `dev` at `eab2f93`; remote raw manifests and GitHub validation pass
- Base: `dev` at `5abc48c`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.5` to approved immutable `v0.2.0-beta.6`, repairing executable modes after registry extraction and adding authoritative cache health plus persistent maintenance notifications.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.6` resolves to commit `e9e7554f95196a35a55c96672863534d938f0fc4`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, and executable Git modes for both scripts.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, runtime code, or Dispatcharr core behavior.
- Validation: the exact remote tag resolves to `e9e7554`; the downloaded GitHub archive identifies that commit and contains beta.6 under the stable directory with the beta.4 canonical wrapper pin. Development registry validation, all five unit tests, JSON parsing, prior-version retention, complete-diff review, published raw root/detail manifest agreement, and the GitHub manifest workflow pass. The live instance still has beta.5 installed and its last cached registry refresh predates publication, so installed beta.6 validation remains pending.
- Completion: `dev` advertises immutable beta.6 from exact source commit `e9e7554`; beta.5 through v0.1.0 remain indexed, and no `main` or unrelated plugin metadata changed.
