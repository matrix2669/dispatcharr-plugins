# Changelog

Notable user-visible registry changes are recorded here. Plugin behavior and source release notes remain in each plugin's own changelog.

## Unreleased

### Added

- Publish the explicitly approved Dispatcharr Stream Sort `0.3.6` GitHub Release in the stable registry with its exact immutable tag and commit after source, public archive, manual ZIP, checksum, tagged-build registry, and managed-install validation.
- Publish the approved Arr Stack Connector `0.2.0` GitHub Release in the stable registry.
- Document the released and tagged-build registry contracts, branch ledger, decisions, and publication procedure.
- Add automated validation for manifest structure, immutable archive references, version history, and channel-specific URLs.
- Require a fresh official Dispatcharr repository review and compatibility validation whenever the supported or deployed Dispatcharr version changes.

### Changed

- Promote FFmpeg Smart Profiles `0.2.0` to the stable registry from its exact immutable tag and commit under the explicitly approved no-Release exception; retain `0.1.0` history and publish no GitHub Release or distributable ZIP while inherited-wrapper licensing remains unresolved.
- Replace the stable Dispatcharr VOD Newznab listing with the renamed `arr-stack-connector` identity; retain the legacy detail manifest unindexed.
- Rename the tagged-build registry channel from `dev-test` to `dev` after controlled consumer migration.
- Keep each plugin in `dev` on its newest approved tag: beta while testing is active, otherwise the latest completed stable version whether released or not.
- Normalize the registry display names to `matrix2669 Plugins` and `matrix2669 Plugins (dev)`.
- Reconcile `dev` with the stable FFmpeg Smart entry added to `main` after the legacy channel histories diverged.

### Removed

- Retire the legacy `dev-test` channel and completed `feature/registry-workflow` branch after GitHub validation and live Dispatcharr migration.

## 2026-08-22

### Changed

- Keep Dispatcharr Stream Sort out of the stable registry because it has test tags but no approved GitHub Release.
- Advertise Dispatcharr Stream Sort `0.3.6-beta.2` only in the testing registry.
- Remove Mustarrd DVR Handoff from the stable registry while retaining it in testing.

## 2026-08-19

### Added

- Publish FFmpeg Smart Profiles `0.1.0` in the stable registry.

## 2026-08-15

### Changed

- Publish Dispatcharr VOD Newznab `0.1.16` in the stable registry.

## 2026-08-11

### Added

- Initialize the matrix2669 Dispatcharr plugin registry.
- Add the first Mustarrd DVR Handoff registry metadata.
