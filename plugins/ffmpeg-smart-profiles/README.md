# FFmpeg Smart Profiles

Registry metadata for the Dispatcharr FFmpeg Smart Profiles plugin.

Source: `matrix2669/Dispatcharr-FFmpeg-Smart-Plugin`

The plugin creates configurable managed Stream and Output Profiles backed by its bundled hardware-aware FFmpeg wrapper. It supports explicit device overrides, active-job/capacity-based multi-GPU selection, hardware cache rebuilding, real concurrent-stream capacity benchmarking, phase-scoped advanced FFmpeg options, persistent scan notifications, and degraded stream-copy fallback from Dispatcharr's Plugins page.

New installations require a hardware capability scan; updates may require a recheck. Until a required scan completes successfully, managed profiles bypass FFmpeg Smart policy and hardware acceleration and use basic FFmpeg stream copy.

Stable `v0.2.0` is advertised from its exact immutable tag archive under a narrow operator-approved exception. No GitHub Release or distributable plugin ZIP will be created until the bundled wrapper's inherited licensing is resolved.
