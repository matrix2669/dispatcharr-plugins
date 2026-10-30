# FFmpeg Smart Profiles

This work branch prepares `0.2.2-beta.2` for the development registry updater.
It is not published through the dev channel yet: the immutable source tag,
archive and final source-integration gates remain pending. The currently
published development build remains 0.2.1 until an authorized channel update.

The candidate vendors adaptive runtime
`8156f96ce44c2ca0cb0360a8503f7862285b9f23` and provides persisted Off/Auto/Strict
shared startup-input controls, with Off as the default. Auto uses conservative
URL/format-hint handling; it does not detect response format. Strict requires
HTTP MPEG-TS and rejects unsupported input. Source release notes own the full
behavior contract.

After publication, use the configured development repository refresh and normal
Dispatcharr Update action. Registry preparation does not perform installation
or profile actions. Prior immutable versions remain in the detail history.
