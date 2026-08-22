# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-08-22.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | stable channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev-test` | long-lived | retiring | historical registry baseline | `dev` replacement | Existing tagged-build channel retained only until Dispatcharr is verified against `dev`. |
| `feature/registry-workflow` | short-lived | active | `main` | `main` | Add durable registry workflow guidance and manifest validation. |

## Branch Records

### `main`

- Type: long-lived
- Status: active
- Purpose: stable Dispatcharr registry for plugins with explicitly approved GitHub Releases
- Current remote head: `df6b3d3ef0e0791e142544b78e6372aa1b30e970`
- Required publication evidence: user approval, stable source tag, normal GitHub Release, exact source commit, validated install archive, and successful Dispatcharr installation
- Exclusions: beta tags, unreleased plugins, moving source branches, and registry workflow experiments

### `dev-test`

- Type: long-lived
- Status: retiring
- Purpose: legacy name for the continuous tagged-build registry
- Current remote head: `1089ad8fc2b388931cc3dc5466b8674c03e9e171`
- Replacement: `dev`, created from this exact history before manifest URLs are changed
- Deletion gate: publish `dev`, update all testing-channel self-references, switch configured Dispatcharr repositories to the new URL, refresh, install or inspect the advertised builds, and verify no remaining consumer depends on `dev-test`
- Exclusions: do not add new test publications after the `dev` replacement becomes authoritative

### `feature/registry-workflow`

- Type: short-lived
- Status: active
- Base: `main` at `df6b3d3ef0e0791e142544b78e6372aa1b30e970`
- Target: `main`
- Purpose: document the registry-specific standalone workflow and add automated manifest validation
- Scope: `AGENT.md`, `BRANCHES.md`, `CHANGELOG.md`, `DECISIONS.md`, `README.md`, `RELEASE.md`, validator, CI workflow, and lowercase registry display-name normalization
- Exclusions: no plugin publication, plugin version change, archive change, source-code change, GitHub Release, or live Dispatcharr configuration change
- Validation: the current `main` manifest and a transformed `dev-test` snapshot both pass channel validation; all five validator unit tests, Python bytecode compilation, and `git diff --check` pass locally
- Risk: channel rules must not accidentally treat the testing registry as a stable source or merge testing-only plugin entries into `main`
- Expected outcome: reviewable shared repository structure followed by a separately verified `dev-test` to `dev` channel migration

## Planned long-lived branch

`dev` will replace `dev-test` as the continuous tagged-build registry. It is not listed as a current branch until its ref exists. Its initial history must come from the current `dev-test` head so no plugin or version history is lost. Each retained plugin remains present and points to its newest approved beta or completed stable tag.
