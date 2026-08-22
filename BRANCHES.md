# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-22.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `feature/arr-stack-connector-v0.2.0-dev` | feature | active locally | `dev` | `dev` | Advance the development channel from the tested beta to released stable version `0.2.0`. |

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
- Validation: the development validator and all registry tests pass; Arr Stack Connector `0.2.0-beta.1` resolves to the recorded source commit and its published archive contains the required plugin directory. Live Dispatcharr installation testing is pending.

### `feature/arr-stack-connector-v0.2.0-dev`

- Type: feature
- Status: active locally
- Base and target: `dev`
- Purpose: point the Arr Stack Connector development entry to stable tag `v0.2.0` and reuse its released `main` detail manifest
- Scope: development root manifest, changelog, and branch ledger only; preserve the beta detail manifest unindexed
