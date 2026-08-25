# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-24.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `fix/stream-sort-v0.3.6-beta.4` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.4` correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.6` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.6` cancellation and analyzer-serialization correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.9` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.9` combined-capture correction only to the tagged-build channel. |

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
- Current FFmpeg Smart build: corrected beta `0.2.0-beta.2` from source commit `75118a8855b4275f41bd886ec9919ddda81593be`; the immutable tag archive preserves executable `ffmpeg-smart-profiles/ffmpeg-smart-plugin.sh` and `ffmpeg-smart.sh`. The development validator and registry tests pass, and Dispatcharr's managed update from recorded `0.1.0` preserved external state across directory replacement before successful recache, restart, and 10-second 4K30 `pipe:0` validation.
- Current Stream Sort build: corrective beta `0.3.6-beta.9` from source commit `9eea52417c1f2f25307f9d52825bd41a22fb2bb7`; the immutable tag archive preserves `stream_sorter/plugin.json`, reports the synchronized beta.9 version, compiles, and passes all 129 source tests. Combined capture failures retry content and throughput together, log per-stream errors, preserve accurate baseline reasons, and do not create completion TTL evidence without a valid sample.
