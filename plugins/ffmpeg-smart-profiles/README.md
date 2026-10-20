# FFmpeg Smart Profiles

Registry metadata for the Dispatcharr FFmpeg Smart Profiles plugin.

Source: `matrix2669/Dispatcharr-FFmpeg-Smart-Plugin`

The plugin creates configurable managed Stream and Output Profiles backed by its bundled hardware-aware FFmpeg wrapper. It supports explicit device overrides, active-job/capacity-based multi-GPU selection, hardware cache rebuilding, real concurrent-stream capacity benchmarking, phase-scoped advanced FFmpeg options, persistent scan notifications, and degraded stream-copy fallback from Dispatcharr's Plugins page.

New installations require a hardware capability scan; updates may require a recheck. Until a required scan completes successfully, managed profiles bypass FFmpeg Smart policy and hardware acceleration and use basic FFmpeg stream copy.

Historical `v0.2.0` remains in version history under its original narrow no-Release exception; those artifacts are not repackaged or relicensed.

Stable `v0.2.1` uses the independently licensed MIT ffmpeg-adaptive runtime and
normal GitHub Release publication with manual-install ZIP and SHA-256. The
registry installs the verified immutable v0.2.1 tag archive. Historical v0.2.0
rights/artifacts remain unchanged; its no-Release exception is no longer the
current publication path. The stable plugin retains tested runtime commit
913a958fd5f9edc231c49a70539a09f611fdcc5a, independent of standalone adaptive
0.1.0. No running installation is changed by registry publication.
