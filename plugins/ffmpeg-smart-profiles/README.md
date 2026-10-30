# FFmpeg Smart Profiles

The development registry advertises `0.2.2-beta.2` using immutable source tag
`v0.2.2-beta.2` at `3b7f554c0aac64391768e4920178cacd6a15da8c`.
The stable registry and installed plugins are unchanged by this publication.

The candidate vendors adaptive runtime
`8156f96ce44c2ca0cb0360a8503f7862285b9f23` and provides persisted Off/Auto/Strict
shared startup-input controls, with Off as the default. Auto uses conservative
URL/format-hint handling; it does not detect response format. Strict requires
HTTP MPEG-TS and rejects unsupported input. Source release notes own the full
behavior contract.

After publication, use the configured development repository refresh and normal
Dispatcharr Update action. Registry preparation does not perform installation
or profile actions. Prior immutable versions remain in the detail history.

