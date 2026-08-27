# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-26.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | stable channel | Advertise approved stable builds, normally backed by GitHub Releases, plus the exact FFmpeg Smart `v0.2.0` exception. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `release/ffmpeg-smart-v0.2.0` | release | merged | `main` | `main` | Advertise explicitly approved FFmpeg Smart `v0.2.0` through the stable channel under a temporary no-Release exception. |

## Branch Records

### `main`

- Type: long-lived
- Status: active
- Purpose: stable Dispatcharr registry for plugins with explicitly approved GitHub Releases plus the exact FFmpeg Smart `v0.2.0` exception
- Required publication evidence: normally user approval, stable source tag, normal GitHub Release, exact source commit, validated install archive, and successful Dispatcharr installation; FFmpeg Smart `v0.2.0` instead requires its dedicated exception, exact tag/commit/archive, complete beta/stable validation, and explicit no-Release instruction
- Exclusions: beta tags, completed-but-unreleased versions, moving source branches, and unrelated `dev` entries
- Promotion rule: make a focused change from `main`; never merge the complete `dev` catalog into this branch
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/main/manifest.json`
- Current Arr Stack build: released version `0.2.0` at source commit `2c7441bd4cceb8e2a68b50a0c24b064e87c6eb46`
- Current FFmpeg Smart build: published stable tag `v0.2.0` at source commit `6eb5c8c8f437dcca6802967ceb193e37f984a7c1`, backed by canonical `ffmpeg-asr v1.1.0` commit `448837f4f6267de1c6705cb670bcdb0c6991614f`; no GitHub Release or manual ZIP is authorized.
- FFmpeg Smart validation: exact immutable tag/archive/source-pin inspection, executable launcher/wrapper modes, stable validator, seven registry tests, public raw-manifest agreement, and GitHub workflow `33027725444` pass.
- Workspace governance: `main` contains the mandatory workspace standards reconciliation gate at revision `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.

### `dev`

- Type: long-lived
- Status: merged into and published through `main` at `efcf8c29a4af4b95a97d1f5d0a327b63256889ad`; public raw metadata and workflow `33027725444` pass
- Purpose: continuous tagged-build registry containing the newest approved immutable tag for every retained plugin
- Origin: created from the complete legacy `dev-test` history, then reconciled with stable entries that were added to `main` after the histories diverged
- Versions: beta tags during active testing; completed stable tags after feature or fix completion, whether released or not
- Stable reuse: when the newest tagged version is identical to `main`, the root index reuses the unchanged `main` per-plugin manifest
- Exclusions: moving source branches, untagged builds, and implicit promotion to `main`
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/dev/manifest.json`
- Validation: GitHub manifest validation passed and Dispatcharr loaded all four expected entries after the channel migration

### `release/ffmpeg-smart-v0.2.0`

- Type: focused stable-channel publication branch
- Status: active
- Base: `main` at `f37db36fad4f2e7592704cfec7c046c948c9a370` after refreshing the registry and source repositories.
- Target: `main` only; never merge the complete `dev` channel.
- Purpose: advertise the fully validated plugin stable tag `v0.2.0` while preserving every unrelated stable entry.
- Scope: root/detail FFmpeg Smart metadata, exact stable tag/commit/archive URL, retained immutable history, scan guidance, the user-approved no-Release exception, changelog, decisions, and branch records.
- Exclusions: no GitHub Release, manual ZIP, checksum asset, license claim, beta or unrelated plugin promotion, Dispatcharr compatibility-floor change, or `dev` channel merge.
- Approval: the user explicitly approved this exact stable manifest publication on `2026-08-26` and directed that no GitHub Release be created until licensing is resolved.
- Completion: stable source tags, source/plugin validation, immutable archive inspection, main-registry validation, public raw-manifest verification, and GitHub workflow validation pass. Prior installed beta.11 testing covered the identical runtime tree; no GitHub Release or manual ZIP was created.
