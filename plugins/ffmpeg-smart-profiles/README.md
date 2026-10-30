# FFmpeg Smart Profiles

The development updater advertises **0.2.2-beta.3**, immutable tag
`v0.2.2-beta.3` at `b3f11557887b7e7388d3589a87646a049fe5d586`.
Refresh the development repository in Dispatcharr, then use its normal Update
action. Publication does not install the plugin or modify saved profiles.

The copy-codec text field defaults blank, meaning the current validated cache
preference. Explicit lists such as `h264, mpeg2` choose copy-eligible codecs.
Legacy `mpeg2video` remains compatible. Conversion uses the cached preference
unless explicitly overridden; the dedicated conversion selector is removed.
Shared input is automatic where supported, with64MiB retained payload and10s
startup watchdog. Removed settings migrate when Install or Update Profiles runs.
See source release notes for transport fallback and independent I/O guard limits.
Stable registry main and prior immutable version history are unchanged.
