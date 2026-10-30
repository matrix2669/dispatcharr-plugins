# DEPENDENCIES.md

This registry contains metadata only. The plugin source repository owns runtime
code, tags, archives, tests, and release artifacts; Dispatcharr owns the
consumer-side manifest and archive-loading contract.

## FFmpeg Smart beta.2 preparation (2026-10-30)

- WIP proposed source: `3b7f554c0aac64391768e4920178cacd6a15da8c`; tag `v0.2.2-beta.2` absent at preparation.
- Runtime pin: `8156f96ce44c2ca0cb0360a8503f7862285b9f23`; parent supplied accepted plugin CI `41081772056`, runtime CI `41081025179` and independent source review.
- Parent refreshed plugin dev and confirmed it is an ancestor of accepted `3b7f554`; plugin CI `41081772056` is successful at that exact SHA. Beta.1 is not represented as a historical registry publication: existing dev metadata advertises 0.2.1.
- Verify final source dev/tag and exact CI before publication; then download the precise advertised tag archive, record SHA-256, check version/runtime byte identity/layout and disposable official install/update behavior. Proposed timestamp `2026-10-30T15:54:31Z` derives from candidate source commit. No archive digest is invented.
- Minimum Dispatcharr `v0.29.0` remains unchanged. Existing reviewed 0.32.0/0.31.0 contracts below remain historical evidence; any changed supported/tested/deployed version requires a current official consumer review.
- Registry preparation, dev publication, repository refresh and managed installation are distinct states. Direct installation is excluded by operator correction; no live action occurred during this preparation.

## FFmpeg Smart Profiles

- Source repository: `matrix2669/Dispatcharr-FFmpeg-Smart-Plugin`.
- Registry contract: the development entry must use the exact immutable
  versioned tag (including `v0.2.2-beta.2`) or full commit SHA, matching full and short source
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

- Publication verified: registry `dev` metadata commit `477689a7eda3f2120a133dd119fdc6a8f6191fa3`; exact-commit registry CI `37870739628` passed. Public raw root/detail files equal the reviewed metadata and agree on beta.3 and source SHA. Previous history and unrelated entries are unchanged. Source documentation checkpoint `c46f246c4c2a219c9d72ca7309a15c1777aa35fc` also passes CI (`37870723593`, `37870723147`); it does not alter the tagged beta source. Live installation remains pending user action.


### Publication evidence superseding preparation above

Final source/tag: 3b7f554c0aac64391768e4920178cacd6a15da8c,
v0.2.2-beta.2, exact complete CI41085032947 passed. Runtime pin remains
8156f96ce44c2ca0cb0360a8503f7862285b9f23 (CI41081025179).
Downloaded tag archive SHA256
93134cc3b391b01bd747fd792f9f82e1f9b859aa63a79d771e7574a792d8bb2c.
Compared every packaged file to accepted source. Isolated tests extracted the
exact official Dispatcharr0.33.0 installer functions from
2fa13a6707bdf0dae87e0c494bcd3ca282cdeb3e: clean stable installation and beta.2
atomic replacement, imported version, executable repair, pinned dependency
hashes and prerelease inequality passed. Full Django/database managed update is
not claimed. No direct live installation or settings mutation is authorized.

## Beta.3 publication evidence — 2026-10-30

Source/tag b3f11557887b7e7388d3589a87646a049fe5d586 / v0.2.2-beta.3; runtime
137103b0b5d2ed2f21976c65be2cd5bc816dbdb6. Exact source CI41091130641 and
runtime CI41090068901 passed; independent implementation/package review accepted.
Downloaded tag archive SHA256
4ed267a3fb3e5b1fc65974f2899e68ff55bb7f9e3f2da45e21968be69f4f0f4b.
Every packaged file matches source; all eight runtime pins pass. Isolated actual
installer functions from official Dispatcharr0.33.0 commit
2fa13a6707bdf0dae87e0c494bcd3ca282cdeb3e pass beta.2 clean extraction then
beta.3 overwrite, imported version, executable repair and prerelease comparison.
This tests filesystem/import behavior, not a live database-managed update.
The compatibility target and minimum version have not changed since beta.2.

## Beta.4 updater publication — 2026-10-30

Final source/dev/tag `66f4a620ac8682dcd2d6161ee16d327b8bb81dc1`,
`v0.2.2-beta.4`, passed full exact-source CI41105638669. Runtime pin remains
`bb834684eb2c513e832c43ba6dbc773d5af10cbc` (CI41103493960); source and package
review accepted, isolated588 tests proved one upstream request and1.59/1.48s
startup. Final documentation-only commit retains all tested runtime bytes.

Downloaded tag archive SHA256:
`d5130f6c2d6b7a219d669529fa552153e73b50b227d49032890381969e25f741`.
Every packaged file matches final source. Isolated actual installer functions
from official Dispatcharr0.33.0 commit2fa13a6707bdf0dae87e0c494bcd3ca282cdeb3e
passed beta.3 extraction followed by beta.4 overwrite, imported version, script
permission repair, all eight runtime hashes and prerelease update detection.
No compatibility target/minimum change or live database-managed update claimed.
Registry validator and all seven tests passed; prior history and unrelated
entries were compared and preserved. Direct installation remains excluded.
