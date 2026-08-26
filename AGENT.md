# AGENT.md

## Workspace Standards Reconciliation Gate

Before any substantive work, locate the maintained local `matrix2669/workspace` checkout and run `<workspace>/scripts/reconcile-standards --check .` from this repository root. The workspace `AI-INSTRUCTIONS.md`, `AGENT-STANDARD.md`, and Git history must be available.

If `WORKSPACE-STANDARDS.yaml` is missing, pending, or stale, stop project work and run `<workspace>/scripts/reconcile-standards --diff .`. Review the standards change against this complete `AGENT.md`, `DECISIONS.md`, code/configuration contracts, dependencies, `BRANCHES.md`, `RELEASE.md`, upstream requirements when applicable, and related projects.

A contradiction blocks work. Ask focused follow-up questions to establish whether the changed standard, proposed work, new answer, or older accepted decision is authoritative; never choose silently. Record project-decision supersessions in `DECISIONS.md` and realign every affected artifact. Only after no contradiction remains, run `<workspace>/scripts/reconcile-standards --apply --confirm-reviewed-no-conflicts .`.

Missing workspace standards or Git history is a hard block. Standards exceptions require explicit user authorization and must be stated in a dedicated section of this file with exact scope, rationale, authority, approval date, and review/removal trigger; `DECISIONS.md` cannot waive workspace standards.


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
- short-lived `feature/*` and `fix/*` branches start from the channel they intend to change and return only to that channel.

Do not merge `dev` wholesale into `main`. Promote one explicitly approved plugin release by making a focused stable-manifest change based on `main`. Stable-only removals or corrections likewise remain focused on `main` unless the same change is intentionally needed in `dev`.

Track every current branch in `BRANCHES.md`. Before deleting a branch, preserve user-visible results in `CHANGELOG.md` and significant rationale in `DECISIONS.md`, then remove its ledger entry.

## Session Completion and Remote Continuity

GitHub is the authoritative continuation source. Start by fetching `origin` and resume from the exact remote head of the branch that owns the metadata change. A repository-change request authorizes checkpoint commits and pushes to an isolated branch based on the one channel it may eventually modify. Before ending or handing off a session, preserve unrelated entries, update branch and validation records, run the applicable gates, commit every in-scope committable change, push every local commit, and verify through a fresh remote query that the exact GitHub head matches the intended local checkpoint. Incomplete work is pushed as explicit WIP with failures or unavailable validation recorded; never commit credentials, generated archives, runtime code, machine state, or unrelated metadata merely to clean the worktree.

The checkpoint branch is not a registry channel and does not change what Dispatcharr installs. The checkpoint does not authorize merging into `dev` or `main`, publishing a plugin tag or Release, changing a registry channel, deploying, force-pushing, or deleting a branch. Report the work branch, target channel, source tag, source Release, registry merge, and installed state separately.

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
