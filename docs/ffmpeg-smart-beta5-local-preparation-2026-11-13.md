# Smart beta.5 development manifest preparation, 2026-11-13

Base registry dev: `4e05b83efc2d88da6dd63a9b4d3193ccf75bdfeb`.
Local plugin candidate: `57bef76032ed33300fbcecdd424df4174c099d79`.
Proposed plugin version/tag: `0.2.2-beta.5` / `v0.2.2-beta.5`.
Canonical runtime: `fd6c400d49cff305df7c41a4149d2f00b80355bb`.

## Changes and completed local evidence

Root latest_version/latest_url and Smart detail latest/history identify the same
new plugin candidate. The build timestamp derives from its exact local commit.
The new record is prepended; comparison against the base confirms all previous
version records and all unrelated root entries are identical. Minimum Dispatcharr
v0.29.0, plugin identity and registry-dev URLs remain unchanged.

`python3 scripts/validate_registry.py --channel dev` and all seven validator tests
passed. Plugin preparation separately passed all 80 plugin tests, required
syntax/JSON/compilation gates, idempotent official sync and remote/offline source
checks for all eight files. The exact local manual package was inspected for
stable directory layout, MIT notice, module hashes/modes and imported version.
Its extracted launcher passed normalized six-channel AAC through pipe:0 and
three late-join offsets. These are isolated fixtures, not a live DB update.

Local manual ZIP SHA-256:
`2c597fdd604f58a0b150c6217ac735fa514a1636b471663e8b814ffc5e475218`.
This is not the digest of the future GitHub tag-addressed registry archive.
The local handoff artifacts are under
`/workspace/ffmpeg-smart-beta5-local-evidence/`.

## Unmet publication gates and authorization boundary

No additional repository has been pushed. The proposed tag is absent remotely,
and no registry channel, installed plugin or live setting changed. This prepared
manifest is not advertised and its future URL must not be presented as already
available. Before publication, obtain specific approval, refresh refs/standards,
run complete exact-plugin CI, create/verify the new immutable tag at the accepted
plugin SHA, inspect/download the actual advertised remote archive and record its
digest, then complete exact-registry CI and the approved focused dev update.

Stable/main publication, GitHub Release, direct deployment, profile reconciliation
and live 505 acceptance are excluded. No new Dispatcharr version is used here;
existing compatibility contracts are retained, not newly claimed as verified.
