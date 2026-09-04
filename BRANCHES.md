# Branches

This ledger records every current branch on `matrix2669/dispatcharr-plugins`. GitHub remains authoritative for live refs, commits, pull requests, and checks. Status below was last refreshed on 2026-09-04.

Before deleting a branch, record user-visible results in `CHANGELOG.md` and durable rationale in `DECISIONS.md` when applicable, then remove its index row and detailed record.

## Branch Index

| Branch | Type | Status | Base | Target | Purpose |
|---|---|---|---|---|---|
| `main` | long-lived | active | historical repository root | released channel | Advertise only explicitly approved plugin GitHub Releases. |
| `dev` | long-lived | active | preserved legacy tagged-build history | independent tagged-build channel | Advertise each retained plugin's newest approved immutable tag. |
| `feature/lineuparr-v1.26.2472002-beta.3` | feature | ready | `dev` at `4a64b36` | `dev` | Publish import confirmation and automatic active selection. |
| `feature/lineuparr-v1.26.2472002-beta.2` | feature | published | `dev` at `be8e887` | `dev` | Publish explicit generated-lineup import results as sequential beta.2. |
| `feature/lineuparr-v1.26.2472002-beta.1` | feature | published | `dev` at `0067dbd` | `dev` | Advance Lineuparr to the generated-lineup URL import beta. |
| `feature/lineuparr-v1.26.2471558-beta.1` | feature | published | `dev` at `5253442` | `dev` | Add immutable Lineuparr excluded-aliases beta.1 to the development registry. |
| `feature/stream-sort-v0.3.7-beta.1` | feature | published | `dev` at `d266c2f` | `dev` | Publish immutable Stream Sort beta.1 telemetry retention build. |
| `feature/stream-sort-v0.3.6-beta.15` | feature | published | `dev` | `dev` | Publish immutable Stream Sort beta.15 and validate the managed upgrade. |
| `release/stream-sort-v0.3.6-dev` | release | published | `dev` | `dev` | Advance the tagged-build channel to completed stable Stream Sort `0.3.6`. |
| `feature/ffmpeg-smart-v0.2.0-beta.3` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.3` test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.4` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.4` scoped-options test build. |
| `feature/ffmpeg-smart-v0.2.0-beta.5` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.5` inherited-default guidance build. |
| `feature/ffmpeg-smart-v0.2.0-beta.6` | feature | merged | `dev` | `dev` | Advertise the immutable FFmpeg Smart Profiles `v0.2.0-beta.6` launcher and cache-maintenance correction. |
| `feature/ffmpeg-smart-update-disclaimer` | feature | merged | `dev` | `dev` | Advertise FFmpeg Smart Profiles `v0.2.0-beta.7` with degraded stream-copy fallback and install-versus-update scan guidance. |
| `fix/ffmpeg-smart-v0.2.0-beta.8` | fix | merged | `dev` | `dev` | Replace beta.7 with the immutable corrective beta.8 canonical-wrapper repin. |
| `fix/ffmpeg-smart-v0.2.0-beta.9` | fix | merged | `dev` | `dev` | Restore persistent degraded notification-center reactivation after dismissal. |
| `fix/ffmpeg-smart-v0.2.0-beta.10` | fix | merged | `dev` | `dev` | Refresh persistent degraded notifications from Dispatcharr's authoritative API. |
| `fix/ffmpeg-smart-v0.2.0-beta.11` | fix | merged | `dev` | `dev` | Publish canonical Map All and benchmark-lock corrections for installed validation. |
| `release/ffmpeg-smart-v0.2.0-dev` | release | merged | `dev` | `dev` | Align the tagged-build channel with the completed stable FFmpeg Smart `v0.2.0` build. |
| `feature/ffmpeg-smart-v0.2.1-beta.1` | feature | published | `dev` | `dev` | Advertise the immutable adaptive-probing FFmpeg Smart Profiles `v0.2.1-beta.1` test build. |
| `feature/ffmpeg-smart-v0.2.1-beta.2` | feature | published | `dev` | `dev` | Advertise the modular MIT-runtime FFmpeg Smart Profiles `v0.2.1-beta.2` test build. |
| `docs/ffmpeg-smart-beta2-live-validation` | documentation | integrated | `dev` at `d6495c9` | `dev` | Record managed beta.2 validation without changing registry metadata. |
| `fix/ffmpeg-smart-v0.2.1-beta.3` | fix | published | `dev` at `1adc1fb` | `dev` | Advertise the corrective benchmark/runtime-fidelity FFmpeg Smart Profiles `v0.2.1-beta.3` test build. |
| `docs/ffmpeg-smart-beta3-live-validation` | documentation | integrated | `dev` at `5048952` | `dev` | Record managed beta.3 validation without changing registry metadata. |
| `fix/stream-sort-v0.3.6-beta.4` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.4` correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.6` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.6` cancellation and analyzer-serialization correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.9` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.9` combined-capture correction only to the tagged-build channel. |
| `fix/stream-sort-v0.3.6-beta.10` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.10` telemetry-integrity correction only to the tagged-build channel. |
| `feature/stream-sort-v0.3.6-beta.11` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort `0.3.6-beta.11` adaptive analysis policies only to the tagged-build channel. |
| `feature/stream-sort-v0.3.6-beta.13` | short-lived | merged | `dev` | `dev` | Publish the reviewed Stream Sort split analysis/sorting scopes only to the tagged-build channel. |
| `feature/stream-sort-v0.3.6-beta.14` | short-lived | active | `dev` | `dev` | Publish the reviewed Stream Sort issue #7 settings and scoring controls only to the tagged-build channel. |

## Branch Records

### `feature/lineuparr-v1.26.2472002-beta.3`

- Base: dev `4a64b36f7c64d3bb2b3dc49410b3cadd568c4fc7`; target: dev only.
- Purpose: publish confirmation and automatic activation as sequential beta.3.
- Source: `v1.26.2472002-beta.3` at `7e76a8bae6231c87255b7c447f232aac67c17c45`, remotely verified. Public archive SHA-256: `fe8eea93cfb9d8724b921cb7e74049fdd59fd16dd96ec2adfa0d7262d4248c04`.
- Scope: Lineuparr manifests and publication records; preserve all other plugins and history.
- Status: source and archive validated; registry integration in progress.

### `feature/lineuparr-v1.26.2472002-beta.2`

- Type: short-lived feature publication branch
- Status: published through `dev` at `3b10309d3d39960749cf42149909a2f4c221e915`; workflow `33918110443`, public root metadata, GitHub detail contents, and icon pass
- Base: `dev` at `be8e8870147728736914989e7b2d0ed195fcdcd7`
- Target: `dev` only
- Purpose: advance Lineuparr to immutable sequential `v1.26.2472002-beta.2` so generated-lineup imports report empty and unreachable URLs plus the exact created or refreshed filename
- Source evidence: annotated tag `v1.26.2472002-beta.2` dereferences to `251120aa51d67e555f9c9fba73244c461627c6ec`; downloaded archive SHA-256 is `cc92978b4cad7e7194b0f9d2f37ed1a5543391745f3710954704380a98ca114c` and contains matching runtime and manifest versions, the result-feedback implementation, `lineup_import.py`, and `logo.png`
- Scope: Lineuparr root/detail metadata, retained version history, changelog, decision record, branch ledger, and standards reconciliation only
- Exclusions: unrelated plugin metadata, stable `main`, GitHub Release, deployment, source runtime changes, upstream contribution state, and Dispatcharr core behavior
- Validation: source static validation, generated-import outcome checks, Python compilation, core/client parity, 307-output matcher golden gate, exact remote branch/tag verification, downloaded archive inspection, development registry validation, registry tests, JSON parsing, standards reconciliation, focused diff review, and unrelated-entry preservation
- Completion: `dev` advertises immutable Lineuparr `1.26.2472002-beta.2` from exact source composition `251120aa51d67e555f9c9fba73244c461627c6ec`; registry `main`, deployment, and every unrelated plugin entry remain unchanged

### `feature/lineuparr-v1.26.2472002-beta.1`

- Type: short-lived feature publication branch
- Status: published through `dev` at `77a1ba1f8220832df508f029de5705ac8b44c061`; public manifests, icon, and workflow `33914905385` pass
- Base: `dev` at `0067dbd46d8ae088ec48fc6a66c25e4cf97bb1e5` after workspace standards reconciliation at `sha256:a68828728963dccb02bbc0c02d4aa37efc2c7012e591525890d21a2f462d5f71`
- Target: `dev` only
- Purpose: advance Lineuparr to immutable `v1.26.2472002-beta.1` for development testing of persistent generated-lineup URL import while retaining channel-scoped exclusions
- Source evidence: annotated tag `v1.26.2472002-beta.1` dereferences to `2d13dee93d3d8695662a9e94c9236911718ea34d`; the downloaded GitHub archive contains the expected inner `Lineuparr/` package, matching runtime and manifest versions, `lineup_import.py`, and `logo.png`
- Scope: Lineuparr root/detail metadata, retained version history, changelog, decision record, branch ledger, and standards reconciliation only
- Exclusions: unrelated plugin metadata, stable `main`, GitHub Release, deployment, source runtime changes, upstream contribution state, and Dispatcharr core behavior
- Validation: source static validation, generated-import checks, Python compilation, core/client parity, 307-output matcher golden gate, exact remote branch/tag verification, downloaded archive inspection, development registry validation, all seven registry tests, JSON parsing, standards reconciliation, focused diff review, and unrelated-entry preservation pass
- Completion: `dev` advertises immutable Lineuparr `1.26.2472002-beta.1` from exact source composition `2d13dee93d3d8695662a9e94c9236911718ea34d`; registry `main`, deployment, and every unrelated plugin entry remain unchanged

### `feature/lineuparr-v1.26.2471558-beta.1`

- Type: short-lived feature publication branch
- Status: published through `dev` at `f580dd8f1c1878a35c007fa81fd333e0bbe83dfa`; public manifests, icon, and workflow `33893350037` pass
- Base: `dev` at `5253442ecedd1efdb6593b84a439a688a957b50f` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`
- Target: `dev` only
- Purpose: add immutable Lineuparr `v1.26.2471558-beta.1` for development testing of channel-scoped `excluded_aliases`
- Source evidence: annotated tag `v1.26.2471558-beta.1` dereferences to `f03ea7e1746e48640c94028758ba3325d0ceef62`; the downloaded archive contains the expected `Lineuparr/` package, matching runtime and manifest versions, and `Lineuparr/logo.png`
- Scope: Lineuparr root/detail metadata, changelog, decision record, and this branch ledger only
- Exclusions: unrelated plugin metadata, stable `main`, GitHub Release, manual ZIP, deployment, source runtime changes, and Dispatcharr core behavior
- Validation: source static validation, Python compilation, core/client parity, 307-output matcher golden gate, reachable-history publish audit, exact remote annotated-tag verification, downloaded archive inspection, development registry validation, all seven registry tests, JSON parsing, unchanged unrelated entries, public root/detail manifest agreement, public icon response, and workflow `33893350037` pass
- Completion: `dev` advertises immutable Lineuparr beta.1 from exact source composition `f03ea7e1746e48640c94028758ba3325d0ceef62`; registry `main`, managed Dispatcharr, and every unrelated plugin entry remain unchanged

### `feature/stream-sort-v0.3.7-beta.1`

- Type: short-lived feature publication branch
- Status: published through `dev` at `f757a22848e98931f6488e785f1b341c096b7ec3`; workflow `33706524101` and public manifest verification pass
- Base: `dev` at `d266c2f2cbbd4640c89d850d7db14b06a84af973` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`
- Target: `dev` only
- Purpose: advance Dispatcharr Stream Sort from completed stable `0.3.6` to immutable `v0.3.7-beta.1` for retained media-change, direct-throughput, and applied-sort evidence
- Source evidence: plugin tag `v0.3.7-beta.1` resolves to `8d3afff3bdd0bc0dbc780f211065d81f4da75149`; the public archive reports matching version metadata, contains the expected plugin layout, and passes all 164 tests plus compilation
- Scope: Stream Sort root/detail metadata, preserved version history, registry changelog, and this branch ledger only
- Exclusions: unrelated plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, manual ZIP, stable source promotion, deployment, and Dispatcharr core behavior
- Validation: development registry validator, all seven registry tests, project validation, standards reconciliation, focused diff review, source tag/archive inspection, public root/detail manifests, and workflow `33706524101` pass. Managed repository refresh and installation were not performed because deployment remains separately scoped.

### `fix/ffmpeg-smart-v0.2.1-beta.3`

- Type: short-lived corrective publication branch
- Status: published through `dev` at
  `50489521b1b6350bc95f300ceaf77a8bb7c372da`; public manifests, workflow
  `33333093699`, managed update, cache rebuild, actual-stream matrix, and
  overlapping scheduler validation pass
- Base: `dev` at
  `1adc1fb5986cc4a058bcf9a1bb3ec3d22901bb95` after workspace standards
  reconciliation at
  `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.1-beta.2` to corrective
  immutable `v0.2.1-beta.3`, aligning benchmark and runtime hardware paths,
  bounding capacity searches, and invalidating the superseded cache policy.
- Source evidence: plugin tag `v0.2.1-beta.3` resolves to
  `dd54d4cc82a454135c4eb3b75eeeb5eb48713fe6`; workflow `33333007420`
  passes; the clean archive reports beta.3 and contains the stable plugin
  directory, complete seven-file runtime, MIT notice, and executable launcher
  and entrypoint bits.
- Scope: FFmpeg Smart root/detail metadata, preserved version history, registry
  changelog, decision record, and this branch ledger only.
- Exclusions: no unrelated plugin metadata, Stream Sort, stable `main`, minimum
  Dispatcharr version, GitHub Release, manual ZIP, stable source promotion,
  runtime code, or Dispatcharr core behavior.
- Validation: development validator and seven tests, exact source tag/archive,
  public manifests, and workflow pass. Managed repository 37 updated beta.2 to
  beta.3; the installed seven-file runtime and MIT notice match the tag; retired
  HDR/10-bit controls remain absent; and profile reconciliation was idempotent.
  The old cache became stale, then a rebuild with zero stopped transcodes
  produced valid VAAPI/HEVC capacity 18/reject 19 on the Arc and 14/reject 15
  on the iGPU. Priority-zero 1080p, MPEG-2 1080i, and 720p direct plus finite
  `pipe:0` paths passed with zero decode errors, zero interlaced decoded output
  frames, and monotonic nonnegative DTS. Overlapping jobs used both GPUs. Final
  cache status was valid and no media process remained.

### `docs/ffmpeg-smart-beta3-live-validation`

- Type: short-lived documentation branch
- Status: integrated into `dev` at
  `9564bc8015d3d5efbf69a74f13eb168bbbd1bd4e`; the remote documentation
  branch is retained and no branch deletion is authorized
- Base: `dev` at `50489521b1b6350bc95f300ceaf77a8bb7c372da`
- Target: `dev` only
- Purpose: preserve exact managed beta.3 update, cache-boundary, actual-stream,
  decoded-frame, scheduler, cleanup, and final-process evidence without changing
  the public registry metadata.
- Scope: branch ledger, registry changelog, and ADR-011 provenance only.
- Exclusions: manifests, plugin archives, unrelated plugins, Stream Sort,
  stable `main`, GitHub Release, manual ZIP, stable promotion, and branch
  deletion.

### `feature/ffmpeg-smart-v0.2.1-beta.2`

- Type: short-lived feature publication branch
- Status: published through `dev` at `d6495c932cd53248ac1128b18ebe7a872d1f20f1`; public manifests, workflow `33320510384`, managed update, cache rebuild, and live Stream/Output Profile checks pass
- Base: `dev` at `8113d40c4c17c958f8a5ea8c2620b36b28a8b96d` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.1-beta.1` to approved immutable `v0.2.1-beta.2`, bundling the complete modular MIT `ffmpeg-adaptive` runtime and removing redundant HDR/10-bit plugin controls.
- Source evidence: plugin tag `v0.2.1-beta.2` resolves to `3c7b07cfe2d56540cd319179ef7c0d02318d2d38`; source workflow `33320334916` passes; the clean archive reports beta.2 and contains the entrypoint, six pinned modules, exact dependency MIT notice, and intended executable/read-only modes.
- Scope: FFmpeg Smart root/detail metadata, preserved version history, registry changelog, decision record, and this branch ledger only.
- Exclusions: no unrelated plugin metadata, Stream Sort changes, stable `main`, minimum Dispatcharr version, GitHub Release, manual ZIP, stable source promotion, runtime code, or Dispatcharr core behavior.
- Validation: the development validator, seven registry tests, exact remote archive, public manifests, and workflow pass. Managed repository 37 updated beta.1 to beta.2; the installed seven-file runtime and MIT notice match the tag; retired HDR/10-bit UI fields, saved keys, and options are absent; and a second reconciliation is idempotent. A zero-viewer rebuild produced a valid schema-2 VAAPI/H.264 cache with low-power disabled and measured capacities 15/11. Priority-zero 1080p, 1080i, and 720p sources pass both managed Stream and finite `pipe:0` Output Profile paths with successful full-video decodes and monotonic, nonnegative DTS. Final viewer and FFmpeg-process counts are zero.

### `docs/ffmpeg-smart-beta2-live-validation`

- Type: short-lived documentation branch
- Status: integrated into `dev` at
  `32bb1131dcf2cc84835a0b599d4f6ce5c7c65215`; the remote documentation branch is
  retained and no branch deletion is authorized
- Base: `dev` at `d6495c932cd53248ac1128b18ebe7a872d1f20f1`
- Target: `dev` only
- Purpose: preserve exact registry, managed migration, cache, actual-stream, and
  final process/viewer evidence for FFmpeg Smart Profiles `0.2.1-beta.2`.
- Scope: branch ledger, registry changelog, and ADR-010 provenance only.
- Exclusions: manifests, plugin archives, unrelated plugins, Stream Sort, stable
  `main`, GitHub Release, manual ZIP, stable promotion, and branch deletion.

### `feature/ffmpeg-smart-v0.2.1-beta.1`

- Type: short-lived feature publication branch
- Status: published through `dev` at `503c7c233bb75d7d36883de11925097d7fd95385`; public manifests, workflow, managed update, cache rebuild, HDHomeRun, and CSPAN3 checks pass
- Base: `dev` at `1a954542bcfdeee6d3496ab486314ddadfdc2a7a` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from completed stable `0.2.0` to approved immutable `v0.2.1-beta.1` for adaptive input-probing validation.
- Source evidence: plugin tag `v0.2.1-beta.1` resolves to `d95aaf649b02e23dab76f19d274cb765b75bbca6`; its verified archive reports beta.1, preserves executable launcher/wrapper modes, and pins canonical `ffmpeg-asr v1.1.1-beta.1` commit `ecc64244dae2c0e80761da6f16be92d95b91d29a` at SHA-256 `785a2ffe283452006ffa50d36e12fd2a013f54e0bd233f6d3c8d87f8a46f0f71`.
- Scope: FFmpeg Smart root/detail metadata, imported stable `0.2.0` plus preserved beta history, registry changelog, decision record, and this branch ledger only.
- Exclusions: no unrelated plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: source and plugin local gates, immutable tag/archive inspection,
  development registry validation, public manifests, managed update, cache
  rebuild, HDHomeRun, and CSPAN3 HE-AACv2 checks pass; workflow and deployment
  evidence remain immutable historical inputs to beta.2.


### `release/ffmpeg-smart-v0.2.0-dev`

- Type: short-lived release-alignment branch
- Status: merged into and published through `dev` at `08ae191641105337144edd6f7d64bec488afe9f7`; public raw metadata and workflow `33027886842` pass
- Base and target: `dev`
- Purpose: replace the completed FFmpeg Smart beta.11 entry with stable `v0.2.0`, reusing the exact `main` detail manifest because both channels advertise the identical immutable build.
- Scope: the `dev` root FFmpeg Smart entry, registry changelog, and this branch ledger only.
- Exclusions: no unrelated plugin metadata, no duplicate stable detail manifest, no source code, no GitHub Release, and no distributable ZIP.
- Source evidence: plugin tag `v0.2.0` resolves to `6eb5c8c8f437dcca6802967ceb193e37f984a7c1`, with canonical `ffmpeg-asr v1.1.0` at `448837f4f6267de1c6705cb670bcdb0c6991614f`.
- Completion: `dev` advertises stable `0.2.0`, reuses the exact `main` detail manifest, preserves beta.11 detail metadata as unindexed history, and passes the seven-test validator suite plus public raw-manifest verification.

### `feature/ffmpeg-smart-update-disclaimer`

- Type: short-lived feature branch
- Status: merged into `dev` at `4b9d4a5` and published through `dev` at `f885da0`; remote raw manifests and GitHub validation pass
- Base: `dev` at `eab2f93f7c9af0daf425ed17b324e7ddb7d75dc6`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.6` to approved immutable `v0.2.0-beta.7`, while showing that new installations require a hardware capability scan, updates may require a recheck, and managed profiles fall back to basic stream copy until a required scan succeeds.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.7` resolves to commit `600ba14572ab48f4d920c2cfd7ad4ac9fffce787`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, and synchronized beta.7 plugin metadata.
- Scope: FFmpeg Smart root/detail metadata and descriptions, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Related work: `Dispatcharr-FFmpeg-Smart-Plugin` branch `feature/degraded-proxy-fallback`.
- Validation: exact tag resolution and archive layout, synchronized beta.7 plugin metadata, 37 plugin tests, canonical-wrapper validation, remote immutable-source verification, root/detail description agreement, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, complete-diff review, published raw-manifest agreement, and GitHub workflow run `33014922697` pass.
- Completion: `dev` advertises immutable beta.7 from exact source commit `600ba14`; beta.6 through v0.1.0 remain indexed, and no `main` or unrelated plugin metadata changed. Installed-update validation remains pending.

### `fix/ffmpeg-smart-v0.2.0-beta.8`

- Type: short-lived corrective branch
- Status: merged into `dev` at `be35192` and published through `dev` at `2f35359`; remote raw manifests and GitHub validation pass
- Base: `dev` at `e92fc6c` after beta.7 registry publication and evidence recording.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.7` to corrective immutable `v0.2.0-beta.8`, preserving fallback behavior while repinning to green canonical `ffmpeg-asr v1.1.0-beta.6`.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.8` resolves to commit `5309b16ae2440f36238fa5a5426cf2e2ecc9f918`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, synchronized beta.8 metadata, and canonical source commit `aeff09204000f58aa6fdd3a14781935f77a0823a`.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: exact tag/archive/source-pin inspection, 37 plugin tests, plugin and canonical GitHub workflows, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, complete-diff review, published raw-manifest agreement, and registry workflow run `33016050222` pass.
- Completion: `dev` advertises immutable beta.8 from exact source commit `5309b16`; beta.7 through v0.1.0 remain indexed, the install/update scan disclaimer is unchanged, and no `main` or unrelated plugin metadata changed. Installed-update validation remains pending.

### `fix/ffmpeg-smart-v0.2.0-beta.9`

- Type: short-lived corrective branch
- Status: merged into `dev` at `5fe0171` and published through `dev` at `1ddda06`; remote raw manifests and GitHub validation pass
- Base: `dev` at `d3c1271` after beta.8 registry publication and evidence recording.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.8` to corrective immutable `v0.2.0-beta.9`, making every new fallback invocation restore a dismissed notification-center entry immediately instead of producing only a toast.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.9` resolves to commit `d25b44b8999dba3aaeb82e264fb75335bbcacc88`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, synchronized beta.9 metadata, and the explicit `is_dismissed: false` WebSocket payload.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, canonical wrapper, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: official Dispatcharr v0.29.0 notification-contract review, exact tag/archive inspection, 37 plugin tests, source workflow runs, the development registry validator, all five registry tests, JSON parsing, prior-version retention, workspace validation, `git diff --check`, complete-diff review, published raw-manifest agreement, and registry workflow run `33017533957` pass. Installed beta.9 reactivation remains pending.
- Completion: `dev` advertises immutable beta.9 from exact source commit `d25b44b`; beta.8 through v0.1.0 remain indexed, the install/update scan disclaimer is unchanged, and no `main` or unrelated plugin metadata changed.

### `fix/ffmpeg-smart-v0.2.0-beta.10`

- Type: short-lived corrective branch
- Status: merged into `dev` at `ffcdc4f` and published through `dev` at `7169252`; remote raw manifests and GitHub validation pass
- Base: `dev` at `e96f59f895410e601649a7f2672c702b5c556f29` after beta.9 registry publication and evidence recording.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.9` to corrective immutable `v0.2.0-beta.10`, refreshing the browser from Dispatcharr's authoritative notification API after plugin load, a manual status check, and every new degraded fallback invocation.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.10` resolves to commit `2ceb64a178ee626c833c5d5b786f35e8ed86c99f`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, synchronized beta.10 metadata, and Dispatcharr's built-in `notifications_cleared` refresh event.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, canonical wrapper, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: source feature/dev/tag workflows, exact tag/archive inspection, synchronized beta.10 metadata, preserved beta.9-through-v0.1.0 history, development-registry validation, all five registry tests, JSON parsing, workspace validation, complete-diff review, `git diff --check`, public raw-manifest agreement, and registry workflow run `33018930141` pass.
- Completion: `dev` advertises immutable beta.10 from exact source commit `2ceb64a`; beta.9 through v0.1.0 remain indexed, the install/update scan disclaimer is unchanged, and no `main` or unrelated plugin metadata changed. Installed beta.10 validation remains pending.

### `fix/ffmpeg-smart-v0.2.0-beta.11`

- Type: short-lived corrective branch
- Status: merged into `dev` at `34e2c61a6611b525d10a5eb89180b9915311a95e9`; remote raw manifests and GitHub validation pass
- Base: `dev` at `065aff5e96e7ca34eb02137656f97decc4db2a51` after refreshing the registry and confirming workspace standards revision `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.10` to corrective immutable `v0.2.0-beta.11`, preserving MPEG-TS-compatible auxiliary mappings and keeping degraded stream-copy routing authoritative for the full hardware recheck.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin v0.2.0-beta.11` resolves to `80c40ea164e5711dfbc37e8c465e943b9e1ee9ea`; source branch workflow `33024879688`, dev workflow `33024916207`, and tag workflow `33024939375` pass. The reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, executable launcher/wrapper modes, synchronized beta.11 metadata, and canonical `ffmpeg-asr v1.1.0-beta.7` pin.
- Scope: FFmpeg Smart root/detail version metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no description change, other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Validation: exact tag/archive/source-pin inspection, 39 source tests, canonical and plugin GitHub workflows, the development registry validator, all registry tests, JSON parsing, prior-version retention, workspace validation, complete-diff review, `git diff --check`, registry workflow `33025150782`, public raw-manifest agreement, installed executable modes and wrapper checksum, live service-user fallback/notification behavior, completed 18/15 capacity scan, and four-stream Map All with a copied DVB subtitle all pass.
- Completion: `dev` advertises immutable beta.11 from exact source commit `80c40ea`; beta.10 through v0.1.0 remain indexed, the install/update scan disclaimer is unchanged, and no `main` or unrelated plugin metadata changed. Installed settings and managed profiles were restored after validation.
- Started: `2026-08-26`.

### `main`

- Type: long-lived
- Status: merged into `dev` at `af9af1f` and published through `dev` at `36c2e20`; remote raw manifests and GitHub validation pass
- Purpose: released Dispatcharr registry for plugins with explicitly approved GitHub Releases
- Required publication evidence: user approval, stable source tag, normal GitHub Release, exact source commit, validated install archive, and successful Dispatcharr installation
- Exclusions: beta tags, completed-but-unreleased versions, moving source branches, and unrelated `dev` entries
- Promotion rule: make a focused change from `main`; never merge the complete `dev` catalog into this branch
- Registry URL: `https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/main/manifest.json`

### `fix/stream-sort-v0.3.6-beta.4`

- Purpose: publish the reviewed Stream Sort scheduler, TTL, telemetry, and reporting corrections as immutable beta `0.3.6-beta.4`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, and any moving source branch URL
- Completion: validate the full development registry, merge into `dev`, publish `dev`, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.6`

- Purpose: publish the reviewed Stream Sort analyzer-serialization, safe-stop, checkpointing, and provisional-dead retry corrections as immutable beta `0.3.6-beta.6`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, branch ledger, and pending standards-reconciliation records
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to viewer-aware provider capacity
- Source evidence: immutable tag `v0.3.6-beta.6` resolves to `ab9dfd3c28afe61f757cfb6a40cd0217760f09f3`; the downloaded archive preserves `stream_sorter/plugin.json`, compiles, and passes all 107 source tests
- Completion: validate the full development registry, merge into `dev`, publish `dev`, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.9`

- Purpose: publish the reviewed Stream Sort combined-capture retry, completion-accounting, and first-baseline reason corrections as immutable beta `0.3.6-beta.9`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branches, provider-specific scheduling, and report compaction
- Source evidence: immutable tag `v0.3.6-beta.9` resolves to `9eea52417c1f2f25307f9d52825bd41a22fb2bb7`; the downloaded archive preserves `stream_sorter/plugin.json`, reports the synchronized beta.9 version, compiles, and passes all 129 source tests
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm managed installation, and remove this record only after the short-lived remote branch is deleted

### `fix/stream-sort-v0.3.6-beta.10`

- Purpose: publish the reviewed Stream Sort scan-boundary transition and throughput-accounting corrections as immutable beta `0.3.6-beta.10`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to Dispatcharr compatibility metadata
- Source evidence: immutable tag `v0.3.6-beta.10` resolves to `3f62cdeb50bb41ad1d02eec3f05d5fffaad55c44`; the source passed 131 tests, Python compilation, version consistency, diff checks, and workspace standards reconciliation
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm Dispatcharr installs beta.10, and remove this record only after the short-lived remote branch is deleted

### `feature/stream-sort-v0.3.6-beta.11`

- Purpose: publish the reviewed Stream Sort rolling media history, minimum-bitrate retry floor, placeholder segmentation, adaptive dead TTL, and shared freshness policies as immutable beta `0.3.6-beta.11`
- Base and target: current `dev`
- Scope: Stream Sort root/detail manifests, registry changelog, deployment decision, and this branch ledger only
- Exclusions: stable `main`, unrelated plugin entries, moving source branch URLs, and changes to Dispatcharr compatibility metadata
- Source evidence: immutable tag `v0.3.6-beta.11` resolves to `3097708e9db5621db76ef8f6238e20a2e0498234`; the archive preserves `stream_sorter/plugin.json`, reports synchronized beta.11, and the source passes 138 tests, Python compilation, manifest parsing, diff checks, and workspace standards reconciliation
- Completion: validate the full development registry, merge into `dev`, publish `dev`, confirm Dispatcharr installs beta.11, and remove this record only after the short-lived remote branch is deleted

### `feature/stream-sort-v0.3.6-beta.13`

- Type: short-lived feature publication branch
- Status: merged into and published through `dev` at `dfd228f94ff7c1e4212d845a48b7f3a71c6951db`; public raw metadata and registry workflow `33128776643` pass, with managed installation pending.
- Base: `dev` at `ab2e429f53a77b1db5f4d2ad124948ad2179c91e` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`.
- Target: `dev` only
- Purpose: advance Dispatcharr Stream Sort from `0.3.6-beta.12` to approved immutable `v0.3.6-beta.13` for separate Analyze & Sort and Analyze Only channel scopes.
- Source evidence: tag `v0.3.6-beta.13` resolves to `0d83cdb80f882223bceb67ec1afd09d348a4d084`; the verified GitHub archive preserves `stream_sorter/plugin.json`, reports beta.13, and the source passes 154 tests, Python compilation, diff checks, and workspace validation.
- Scope: Stream Sort root/detail metadata, preserved beta.12 and earlier history, registry changelog, and this branch ledger only.
- Exclusions: no unrelated plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior.
- Completion: `dev` advertises immutable beta.13 from exact source commit `0d83cdb`; beta.12 and earlier history remain indexed, the public raw manifests agree, and no `main` or unrelated plugin metadata changed. Managed Dispatcharr installation remains pending and will be reported separately.

### `feature/stream-sort-v0.3.6-beta.14`

- Type: short-lived feature publication branch
- Status: merged into and published through `dev` at `005cdf95900078197621d6615eadb173833d778f`; public raw metadata, registry workflow, and managed installation pass
- Base: `dev` at `430dd5bbed7055c6d409f8cff5b7368b38f5ce17` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`
- Target: `dev` only
- Purpose: advance Dispatcharr Stream Sort from `0.3.6-beta.13` to approved immutable `v0.3.6-beta.14` for issue #7 settings and scoring simplification
- Source evidence: tag `v0.3.6-beta.14` resolves to `250d9d4d7f80b492862819c18622ec23f780e5f9`; the verified GitHub archive preserves `stream_sorter/plugin.json`, reports beta.14, compiles, and passes all 157 source tests
- Scope: Stream Sort root/detail metadata, preserved beta.13 and earlier history, registry changelog, and this branch ledger only
- Exclusions: no unrelated plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior
- Validation: the development registry validator, registry tests, JSON parsing, complete-diff review, public raw-manifest agreement, GitHub workflow `33135322510`, and managed beta.14 installation all pass
- Completion: `dev` advertised immutable beta.14 from exact source commit `250d9d4`; beta.13 and earlier history remained indexed, and no `main` or unrelated plugin metadata changed

### `feature/stream-sort-v0.3.6-beta.15`

- Type: short-lived feature publication branch
- Status: merged into and published through `dev` at `b8eb09120d3ea2fe826ad0992570fc27986a3105`; public raw metadata, registry workflow `33138165588`, and managed beta.15 installation pass
- Base: `dev` at `005cdf95900078197621d6615eadb173833d778f` after workspace standards reconciliation at `sha256:6456d4a722cfca0a03e6bce3d698208c844a114953c62d0fe757789d48f1c794`
- Target: `dev` only
- Purpose: advance Dispatcharr Stream Sort from `0.3.6-beta.14` to approved immutable `v0.3.6-beta.15` for descending M3U score selectors, aligned defaults and scope guidance, and evidence-aware TTL recommendations
- Source evidence: tag `v0.3.6-beta.15` resolves to `e795ecebb4c531b4b801476f43c708dc21c34dee`; the verified GitHub archive preserves `stream_sorter/plugin.json`, reports beta.15, compiles, and passes all 159 source tests
- Scope: Stream Sort root/detail metadata, preserved beta.14 and earlier history, registry changelog, and this branch ledger only
- Exclusions: no unrelated plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Release, distributable ZIP, runtime code, or Dispatcharr core behavior
- Validation: development registry validation, public raw-manifest agreement, workflow `33138165588`, and managed beta.15 installation all pass
- Completion: `dev` advertised immutable beta.15 from exact source commit `e795ece`; beta.14 and earlier history remained indexed, and no `main` or unrelated plugin metadata changed

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
- Current FFmpeg Smart build: beta `0.2.1-beta.3` from source commit `dd54d4cc82a454135c4eb3b75eeeb5eb48713fe6`, whose immutable archive bundles canonical MIT `ffmpeg-adaptive v0.1.0-beta.2` at `4df6c12e395187fc0080f858685a3c6ebd7a8c42`. Source/archive checks, development workflow, managed update, corrected VAAPI/HEVC 18/14 cache boundaries, actual 1080p/1080i/720p Stream plus finite `pipe:0` Output Profile validation, and overlapping both-GPU scheduling pass. Stable `main` remains on `0.2.0`; no GitHub Release, manual ZIP, or stable promotion is authorized.
- Current Stream Sort build: completed stable `0.3.6` from source commit `bbae86f2ded0a1bcd09d2906e0530e70380ce5a4`; the immutable public archive passes all 159 tests, and the tagged-build root/detail manifests preserve beta.15 and all earlier history. Stable `main` publication and managed repository 3 installation also pass.
- Current Lineuparr build: beta `1.26.2472002-beta.2` from source composition `251120aa51d67e555f9c9fba73244c461627c6ec`; source/archive checks, development workflow `33918110443`, public root metadata, GitHub detail contents, and icon verification pass. Stable `main` remains absent, upstream remains the stable production source, and managed installation is pending separate authorization.

### `feature/ffmpeg-smart-v0.2.0-beta.3`

- Type: short-lived feature branch
- Status: merged into `dev` at `660297e` and published through `dev` at `b005781`; remote raw-manifest and GitHub validation checks pass
- Base: `dev` at `739937b`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.2` to the approved immutable `0.2.0-beta.3` tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.3` resolves to commit `59f1c207cf68f9b6e8ca289df6b9188d2b5b2565`; the tag archive contains the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, or runtime code.
- Validation: exact tag resolution and archive layout, dev registry validator, all five registry unit tests, JSON parsing, `git diff --check`, and complete-diff review pass; only FFmpeg Smart metadata, history, changelog, and this ledger change.

### `feature/ffmpeg-smart-v0.2.0-beta.4`

- Type: short-lived feature branch
- Status: merged into `dev` at `1d36df9` and published through `dev` at `877ef8b`; remote raw manifests and GitHub validation pass
- Base: `dev` at `942144b`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.3` to the approved immutable `v0.2.0-beta.4` scoped-options tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.4` resolves to commit `08ce3c5ab13f36a22b03826b4d3a847d39a339b3`; the reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, or runtime code.
- Validation: exact plugin tag resolution and archive layout, development registry validator, all five registry unit tests, JSON parsing, prior-version retention, `git diff --check`, and complete-diff review pass; only FFmpeg Smart metadata, history, changelog, and this ledger changed.
- Completion: `dev` advertises immutable beta.4 from exact source commit `08ce3c5`; the raw root/detail manifests agree, prior immutable versions remain indexed, and the published manifest workflow completed successfully.

### `feature/ffmpeg-smart-v0.2.0-beta.5`

- Type: short-lived feature branch
- Status: merged into `dev` at `a3ae423` and published through `dev` at `73d4fbd`; installed-update validation remains pending
- Base: `dev` at `442a2de`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.4` to the approved immutable `v0.2.0-beta.5` inherited-default guidance tag.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.5` resolves to commit `6fb786ddc01105d3328a49be4224b2e4d759e485`; the reviewed tag archive preserves the stable `ffmpeg-smart-profiles/` directory and all five runtime files.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and branch-ledger corrections only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, or runtime code.
- Validation: exact remote tag resolution to `6fb786d`, downloaded archive layout and beta.5 plugin metadata, development registry validator, all five registry unit tests, JSON parsing, prior-version retention, `git diff --check`, and complete-diff review pass; unrelated plugin entries remain unchanged.
- Completion: `dev` advertises immutable beta.5 from exact source commit `6fb786d`; the raw root/detail manifests agree, beta.4 through v0.1.0 remain indexed, and the published manifest workflow completed successfully.

### `feature/ffmpeg-smart-v0.2.0-beta.6`

- Type: short-lived feature branch
- Status: merged into `dev` at `a3ae423` and published through `dev` at `eab2f93`; remote raw manifests and GitHub validation pass
- Base: `dev` at `5abc48c`
- Target: `dev` only
- Purpose: advance FFmpeg Smart Profiles from `0.2.0-beta.5` to approved immutable `v0.2.0-beta.6`, repairing executable modes after registry extraction and adding authoritative cache health plus persistent maintenance notifications.
- Source evidence: `Dispatcharr-FFmpeg-Smart-Plugin` tag `v0.2.0-beta.6` resolves to commit `e9e7554f95196a35a55c96672863534d938f0fc4`; its reviewed archive preserves the stable `ffmpeg-smart-profiles/` directory, all five runtime files, and executable Git modes for both scripts.
- Scope: FFmpeg Smart root/detail manifest metadata, preserved version history, registry changelog, and this branch ledger only.
- Exclusions: no other plugin metadata, stable `main`, minimum Dispatcharr version, GitHub Releases, distributable ZIPs, runtime code, or Dispatcharr core behavior.
- Validation: the exact remote tag resolves to `e9e7554`; the downloaded GitHub archive identifies that commit and contains beta.6 under the stable directory with the beta.4 canonical wrapper pin. Development registry validation, all five unit tests, JSON parsing, prior-version retention, complete-diff review, published raw root/detail manifest agreement, and the GitHub manifest workflow pass. The live instance still has beta.5 installed and its last cached registry refresh predates publication, so installed beta.6 validation remains pending.
- Completion: `dev` advertises immutable beta.6 from exact source commit `e9e7554`; beta.5 through v0.1.0 remain indexed, and no `main` or unrelated plugin metadata changed.

## FFmpeg Smart v0.2.1-beta.1 live validation (2026-08-27)

- Registry deployment: dev at `503c7c233bb75d7d36883de11925097d7fd95385`.
- Plugin artifact: `v0.2.1-beta.1` at `d95aaf649b02e23dab76f19d274cb765b75bbca6`.
- Canonical wrapper: `v1.1.1-beta.1` at `ecc64244dae2c0e80761da6f16be92d95b91d29a`; installed SHA-256 `785a2ffe283452006ffa50d36e12fd2a013f54e0bd233f6d3c8d87f8a46f0f71`.
- Managed Install/Update action completed with both profiles unchanged and no conflicts; saved non-probe settings were preserved.
- Hardware cache rebuilt successfully; verified capacities were 15 streams on renderD128 and 18 streams on renderD129.
- HDHomeRun stream 185235 selected the fast 1s/1MB tier and produced 7,333,880 bytes during the bounded live check.
- TVEverywhere CSPAN3 stream 193352 detected incomplete fast-tier audio metadata, selected the expanded 2s/2MB tier, and produced 7,702,924 bytes during the bounded live check.
- Both live processes accepted normal termination with no orphan FFmpeg processes. Stable release publication remains excluded pending the documented licensing resolution.

### `release/stream-sort-v0.3.6-dev`

- Type: short-lived stable tagged-build publication branch
- Status: merged into and published through `dev` at `46e8e884f6ec4f72f6041f426348e332a2f21d05`; public raw metadata, workflow `33138596704`, and managed stable installation pass
- Base: `dev` at `b8eb09120d3ea2fe826ad0992570fc27986a3105` after beta.15 publication and managed-install validation passed
- Target: `dev` only
- Purpose: advance the tagged-build channel from beta.15 to completed stable Stream Sort `0.3.6` while preserving all immutable beta and stable history
- Source evidence: stable tag `v0.3.6` resolves to `bbae86f2ded0a1bcd09d2906e0530e70380ce5a4`; source `main` contains the release at `d16af98828fa8428cccea73e7dda672f7998fe24`; GitHub Release is public with a verified manual ZIP and checksum
- Scope: Stream Sort root/detail stable metadata, preserved history, registry changelog, and this branch ledger only
- Exclusions: no unrelated plugin metadata, stable registry `main`, minimum Dispatcharr version, runtime code, or Dispatcharr core behavior
- Validation: development registry policy, seven tests, JSON parsing, standards reconciliation, public raw-manifest agreement, workflow `33138596704`, and managed stable installation through repository 37 all pass
- Completion: `dev` advertises completed stable `0.3.6` from exact source commit `bbae86f2ded0a1bcd09d2906e0530e70380ce5a4`, retains beta.15 and earlier history, and the installation was subsequently moved to stable repository 3 after `main` publication
- Started: `2026-08-27`
