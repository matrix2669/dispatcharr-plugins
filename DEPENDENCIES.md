# DEPENDENCIES.md

This registry contains metadata only. The plugin source repository owns runtime
code, tags, archives, tests, and release artifacts; Dispatcharr owns the
consumer-side manifest and archive-loading contract.

## FFmpeg Smart Profiles

- Source repository: `matrix2669/Dispatcharr-FFmpeg-Smart-Plugin`.
- Registry contract: the development entry must use the exact immutable
  `v0.2.1-beta.N` tag (or full commit SHA), matching full and short source
  commit IDs in the detail manifest. The root and detail entries must agree on
  name, slug, repository, version, archive URL, and minimum Dispatcharr version.
- Beta.5 publication contract: the immutable tag, tag-archive proof, and
  synchronized registry metadata are verified below. Registry publication and
  live update/benchmark state remain separate operational outcomes.
- Published evidence: plugin tag `v0.2.1-beta.5` resolves to
  `a5c0777875056591e4e02c989993f43b3f43aa72`; exact-SHA CI `35631536698` and
  tag validation `35631993818` passed. The advertised tag archive URL is
  `https://api.github.com/repos/matrix2669/Dispatcharr-FFmpeg-Smart-Plugin/zipball/v0.2.1-beta.5`,
  with SHA-256
  `db31ce469ea52433af24cf4568463a782fced202124cdf3440c854fcf9754836`.
  The archive equals the reviewed full-commit archive and passed the official
  Dispatcharr `0.31.0` native installer harness. The wrapper tag
  `v0.1.0-beta.4` resolves to
  `913a958fd5f9edc231c49a70539a09f611fdcc5a`; wrapper CI run `35633440274`
  passed with workflow-definition SHA
  `10a6e4b8e16b66857df3b03a7bb6d0bb88fc9929`, unchanged-tag source checks,
  ShellCheck 0.11, checksum, complete-suite, and clean-tree assertions.
- Reviewed repair scope: beta.4's version-reporting loop, benchmark diagnostic
  I/O/cache false-success paths, subprocess result propagation, stale tracking
  reference, stdout leak, and stale/admission cleanup defects pass the reviewed
  automated, native installer, managed-update, and zero-viewer benchmark checks.
- Canonical adaptive runtime: beta.5's wrapper tag and exact source pin are
  verified above against the published archive and completed wrapper CI.

## Dispatcharr consumer

- The registry currently records minimum Dispatcharr `v0.29.0`; no beta.5
  change to that value is authorized by this preparation work.
- The reviewed registry contract requires immutable archive references,
  matching root/detail metadata, expected plugin layout after archive
  extraction, semantic-version comparison, and install/update version
  agreement. The current compatibility refresh reviewed official Dispatcharr
  [`v0.31.0`](https://github.com/Dispatcharr/Dispatcharr/tree/bcbb68c4f054ee56383a41604cfcd7302b85da66)
  at commit `bcbb68c4f054ee56383a41604cfcd7302b85da66`, with installed version
  `0.31.0`; live installed loader, API-view, and serializer file hashes matched
  the corresponding official source files at that commit. The installer,
  rather than the loader, discovers the shallowest `plugin.py`, normalizes
  hyphens to underscores, retains nested library files, and strips archive
  modes; beta.5 publication must therefore verify executable-mode repair in the
  installed package. Prerelease comparison uses exact equality, and discovery
  can overwrite the requested install version with `Plugin.version`; managed
  update preserves settings/enabled state with `force_reload`. The exact
  Dispatcharr source revision must be refreshed and recorded before a
  supported/minimum/tested version changes.

## Evidence status

Current evidence includes the published beta.5 source/archive and Dispatcharr
`0.31.0` installer validation above. Registry publication is complete through
`dev` at `1e55f15ba3824f85209258b6b0dd3280c554924d`; public metadata and
registry CI `35633913052` pass. Managed update and zero-viewer benchmark
completed with settings/enabled preservation, valid cache, no PID/lock, and no
residual media processes. Detailed plugin evidence is recorded in
[the plugin validation report](https://github.com/matrix2669/Dispatcharr-FFmpeg-Smart-Plugin/blob/dev/docs/beta5-validation-2026-09-21.md). Stable promotion and GitHub Release remain
excluded.

## Mustarrd DVR Handoff zero-handoff beta.3

- Approved development tag: `v0.2.13-beta.3`, source commit `c5adaf5215daba6ea7211c9a5257b4f2beb8237f`, annotated tag object `8b5727062277f976b647d3940151369103e8f99e`.
- Exact-source CI passed: work branch run `37870492937`, source `dev` run `37870578490`, tag run `37870578514`; all run `Validate plugin` against the same source SHA.
- Published archive: `https://api.github.com/repos/matrix2669/Dispatcharr-Mustarrd-DVR-Plugin/zipball/v0.2.13-beta.3`; SHA-256 `90899f25f6696f07ed895f845bc1e4dc3163407b1990dbe66dac6e9323b6bbf5`. Runtime files byte-match the exact tag; the immutable icon matches the archive.
- Disposable official Dispatcharr `v0.31.0` installer and loader at freshly verified `bcbb68c4f054ee56383a41604cfcd7302b85da66` pass installation, beta.2 overwrite, runtime/manifest version discovery, default merging, update comparison and installed-package retention regressions. External framework/database boundaries are stubbed; no live service or recording is contacted. Minimum `v0.29.0` is unchanged.
- Source tests: all 23 pass. Registry validator and seven tests pass. Production Mustarrd dependency audit remains open; beta publication does not clear it. Managed installation is outside authorization.
