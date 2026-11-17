# AGENT.md

## Local Smart beta.6 preparation boundary, 2026-11-13

The owner authorizes local plugin and registry preparation for the Add audio
chain correction. Prepare only the next beta.6 root/detail metadata, preserving
all history and unrelated entries. No push, channel integration, tag, installed
update, live profile change or deployment is authorized. This explicit direction
supersedes routine checkpoint-push guidance. Later publication must verify exact
canonical/plugin CI, immutable source/tag/archive and registry CI in order.

## Workspace Standards Reconciliation Gate

Before substantive work, refresh the maintained `matrix2669/workspace` checkout and check current standards against this repository's applied `WORKSPACE-STANDARDS.yaml`. Reconcile changes before proceeding, and recheck before integration or channel publication.

At the pre-work check and those publication boundaries, locate the maintained matrix2669/workspace checkout and run
`<workspace>/scripts/reconcile-standards --check .`. Review `--diff` against the
complete project guidance, accepted decisions, code/configuration/dependency and
branch/release contracts. Resolve contradictions explicitly before applying
`--apply --confirm-reviewed-no-conflicts`. Missing authoritative standards/history
blocks the affected substantive work or publication. Never advance the fingerprint merely to silence a check.
Exceptions require explicit scope, authority and review criteria here.

Validation evidence is exact-commit scoped. Reuse a complete original successful
run only for the same commit and acceptance inputs; a different SHA requires fresh
validation. Preserve approval provenance across delegation without broadening it.
Checkpoint publication is distinct from integration, release and installation. This is a standalone repository: keep its branch, decision, changelog and validation records here. Do not create a workspace status record or workspace-main closeout for registry publication. Deletion and force pushes remain separate.

## Purpose

This repository is the matrix2669 Dispatcharr plugin registry. It maps two branch-backed distribution channels to immutable builds owned by separate plugin source repositories.

It contains metadata only. Do not add plugin runtime code, build outputs, credentials, or machine-specific state.

## Architecture

- `manifest.json` is the channel index consumed by Dispatcharr.
- `plugins/<slug>/manifest.json` is the complete version history and current publication metadata for one plugin in that channel.
- `plugins/<slug>/README.md`, when present, contains plugin-specific registry notes for users.
- `scripts/validate_registry.py` validates channel identity, cross-file consistency, semantic versions, immutable archive references, and version history.
- `.github/workflows/validate-manifests.yml` applies the validator according to the target channel.

Plugin source repositories remain authoritative for code, tags, GitHub Releases, release artifacts, and plugin changelogs. This registry is authoritative only for which immutable build each configured channel advertises.

## Branch and Channel Workflow

This standalone metadata repository follows the workspace's supported metadata-registry profile:

- `main` is the stable Dispatcharr registry.
- `dev` is the continuous tagged-build registry. It advertises the newest approved tag for each plugin, whether that tag is a beta or a completed stable version.
- Per the owner's 2026-11-15 direction, only `main` and `dev` may exist. Make scoped authorized channel updates directly; do not create feature or fix branches in this metadata registry.

Do not merge `dev` wholesale into `main`. Promote one explicitly approved plugin release by making a focused stable-manifest change based on `main`. Stable-only removals or corrections likewise remain focused on `main` unless the same change is intentionally needed in `dev`.

Track every current branch in `BRANCHES.md`. Before deleting a branch, preserve user-visible results in `CHANGELOG.md` and significant rationale in `DECISIONS.md`, then remove its ledger entry.

## Session Completion and Remote Continuity

GitHub is the authoritative continuation source. Refresh the intended channel's remote head and preserve unrelated entries before preparing a change. The owner's two-branch rule forbids isolated registry work branches. Commit scoped metadata locally and run all prepublication gates; push only with explicit channel-publication authority and passing required validation. Never publish incomplete WIP or failed/unavailable validation merely to create a remote checkpoint. If publication is blocked, retain the local candidate and report the blocker instead. Never commit credentials, generated archives, runtime code, machine state, or unrelated metadata. Verify the exact remote channel head after an authorized push and collect its mandatory CI result before declaring completion.

Because only `main` and `dev` exist, pushing either branch publishes that registry channel. Do not treat a registry checkpoint as a non-publishing branch: require explicit scoped channel-publication authority before pushing. That authority does not imply a source tag or Release, live installation/deployment, force-push, or branch deletion. Report the target channel, exact manifest commit, source tag/Release and installed state separately.

## Distribution Rules

- Every plugin retained in the tagged-build channel stays in `dev` and points to its newest approved immutable tag.
- During active testing that tag may use `-beta.N`; after feature or fix completion it advances to the completed stable Semantic Version.
- If no beta is active, keep the plugin on its latest completed stable tag rather than removing it or falling back to a moving branch.
- Beta and completed stable tags in `dev` do not require GitHub Releases.
- When `dev` and `main` advertise the same released plugin version, the `dev` root index may reference that plugin's `main` per-plugin manifest. Do not duplicate a no-op detail-manifest update.
- When `dev` advertises a beta or a completed-but-unreleased stable tag, its root entry must reference a `dev` per-plugin manifest carrying that exact version.
- A tag alone never authorizes stable publication.
- Add a plugin to this repository's `main` branch only after the user explicitly approves and publishes a stable GitHub Release in the plugin source repository.
- An unreleased plugin remains absent from `main`, regardless of how many test tags exist.
- Never move or replace an advertised tag. Publish a new plugin version when correcting an installed build.
- Use an immutable tag or full commit SHA in every archive URL. Never point an install URL at a moving branch.

## Manifest Invariants

- `slug` values are unique in the root manifest and match the per-plugin manifest. The registry directory is derived from `manifest_url` and may differ from the Dispatcharr slug.
- A per-plugin manifest may remain unindexed to preserve historical metadata after a plugin is removed from a channel; only root-indexed entries are advertised to Dispatcharr.
- Root and per-plugin identity, version, repository, minimum Dispatcharr version, and latest archive URL agree.
- `latest_version`, `latest.version`, and the first `versions` entry identify the same build.
- Each full `commit_sha` is 40 lowercase hexadecimal characters and each `commit_sha_short` is its seven-character prefix.
- Version history is newest first, contains no duplicate versions, and retains previously advertised immutable builds.
- `main` uses `matrix2669 Plugins` and `main` manifest URLs.
- The `dev` root uses `matrix2669 Plugins (dev)`. Each entry references either its exact `dev` per-plugin manifest or, when the tagged build is identical to the released channel, the unchanged `main` per-plugin manifest.
- `main` versions are normal Semantic Versions backed by approved GitHub Releases. `dev` versions may be either `-beta.N` prereleases or completed stable Semantic Versions without Releases.

The validator checks structural invariants, but it cannot infer release approval. Before changing `main`, independently verify the exact source tag, GitHub Release, artifact layout, commit, and user approval.

## Dispatcharr Compatibility Refresh Gate

Whenever the supported, minimum, tested, or deployed Dispatcharr version changes, revalidate the manifest contract against the matching current revision of the official Dispatcharr repository before publishing either registry channel.

The review must:

- refresh the official Dispatcharr repository rather than relying on cached requirements;
- identify and record the Dispatcharr version or tag, exact commit, repository URL, and review date;
- inspect the current plugin registry and per-plugin manifest schema, required and optional fields, version comparison behavior, archive download and extraction rules, plugin directory/layout expectations, minimum-version handling, and installation/update API behavior;
- compare those requirements with `manifest.json`, every affected `plugins/<directory>/manifest.json`, `scripts/validate_registry.py`, and the referenced plugin archive;
- update documentation, validation, and manifests when the contract changed;
- run the validator and an installation or update check on the changed Dispatcharr version.

Treat a change to any `min_dispatcharr_version` value or an upgrade of the Dispatcharr instance used for validation as a Dispatcharr version change. If the matching repository revision or current requirements cannot be verified, stop the publication and report the missing evidence; do not present cached requirements as current.

## Publication Procedure

Follow `RELEASE.md`. A registry update is a branch publication, not a release of this repository. This repository intentionally has no `VERSION`, release tags, or GitHub Releases because each manifest entry has its own independently versioned source.

Before review:

```bash
python3 scripts/validate_registry.py --channel main
python3 -m unittest discover -s tests -v
```

Use `--channel dev` for changes based on the testing branch.

## Future Agent Checklist

- [ ] Read `README.md`, `DECISIONS.md`, `BRANCHES.md`, and `RELEASE.md`
- [ ] Refresh all remote branches and confirm the intended target channel
- [ ] Review the affected plugin source repository and its publication state
- [ ] If any Dispatcharr version changed, refresh the official repository and record the exact compatibility review
- [ ] Create or refresh the branch ledger record before substantive work
- [ ] Preserve existing version history and unrelated manifest entries
- [ ] Run the validator for the target channel
- [ ] Verify the exact archive and source commit before publication
- [ ] For `main`, verify explicit release approval and the published GitHub Release
- [ ] Confirm Dispatcharr refreshes and installs the intended version
- [ ] Remove completed short-lived branch records only after their remote refs are deleted

## Development generated archives — owner clarification, 2026-11-15

For development registry publication, trust GitHub-generated archive API output once source, exact tag/version and other checks pass; do not require a separate archive download verification step. Stable release archives retain full verification requirements. This supersedes contrary development-only archive verification wording, not source/CI checks or installation authority.
