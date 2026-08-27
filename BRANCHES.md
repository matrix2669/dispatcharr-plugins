# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-24.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `release/ffmpeg-smart-v0.2.0` | release | active | `main` | `main` | Advertise explicitly approved FFmpeg Smart `v0.2.0` through the stable channel under a temporary no-Release exception. |

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
- Current FFmpeg Smart build: pending focused promotion to completed stable tag `v0.2.0` at source commit `6eb5c8c8f437dcca6802967ceb193e37f984a7c1`; no GitHub Release or manual ZIP is authorized.
- Validation: the stable validator and all registry tests pass; the source Release includes a verified plugin-only ZIP and SHA-256 checksum
- Workspace governance: `main` and `dev` each contain the mandatory workspace standards reconciliation gate at revision `sha256:2717b7fb651e3541b6af68a4793b3c056ea3053bb177e629c97bf2d03a50878f`; this reconciliation changes no registry manifest or plugin publication metadata.

### `dev`

- Type: long-lived
- Status: active
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
- Completion trigger: stable source tags, source/plugin validation, immutable archive inspection, main-registry validation, public raw-manifest verification, and live stable-channel update validation.
