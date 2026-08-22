# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-22.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `feature/mustarrd-dvr-beta-2` | publication | active | `dev` | `dev` | Publish Mustarrd DVR Handoff `0.2.13-beta.2` only to the tagged-build channel. |

## Branch Records

### `main`

- Type: long-lived
- Status: active
- Purpose: released Dispatcharr registry for plugins with explicitly approved GitHub Releases
- Required publication evidence: user approval, stable source tag, normal GitHub Release, exact source commit, validated install archive, and successful Dispatcharr installation
- Exclusions: beta tags, completed-but-unreleased versions, moving source branches, and unrelated `dev` entries
- Promotion rule: make a focused change from `main`; never merge the complete `dev` catalog into this branch
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/main/manifest.json`

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

### `feature/mustarrd-dvr-beta-2`

- Type: short-lived tagged-build publication
- Status: active
- Base and target: `dev`
- Purpose: advance only Mustarrd DVR Handoff from `0.2.13-beta.1` to immutable tag `v0.2.13-beta.2`
- Source commit: `606d2c23775004581c22213b0b1c7ac59e00b4d6`
- Scope: root and per-plugin development manifests, retained version history, changelog, and branch ledger
- Exclusions: registry `main`, GitHub Releases, unrelated plugin entries, and rewriting prior tag metadata
- Required validation: source tag/commit/archive, registry validator, registry tests, and Dispatcharr update detection
