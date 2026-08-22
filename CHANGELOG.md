# Changelog

Notable user-visible registry changes are recorded here. Plugin behavior and source release notes remain in each plugin's own changelog.

## Unreleased

### Added

- Add Arr Stack Connector `0.2.0-beta.1` to the development registry for installation testing under its new plugin identity.
- Document the released and tagged-build registry contracts, branch ledger, decisions, and publication procedure.
- Add automated validation for manifest structure, immutable archive references, version history, and channel-specific URLs.
- Require a fresh official Dispatcharr repository review and compatibility validation whenever the supported or deployed Dispatcharr version changes.

### Changed

- Advance Arr Stack Connector from `0.2.0-beta.1` to released stable version `0.2.0` in `dev`, reuse its matching `main` detail manifest, and retain the beta metadata in an unindexed archive directory.
- Replace the active development listing for Dispatcharr VOD Newznab with the renamed `arr-stack-connector` slug and repository; retain the legacy detail manifest unindexed as historical metadata.
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
