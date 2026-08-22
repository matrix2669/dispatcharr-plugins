# Arr Stack Connector

Development-channel registry metadata for the Dispatcharr Arr Stack Plugin.

Source: `matrix2669/Dispatcharr-Arr-Stack-Plugin`

The plugin exposes raw Xtream VOD variants to Sonarr and Radarr through Newznab Interactive Search, emulates the SABnzbd subset Servarr uses, and hands selected streams to Mustarrd for acquisition.

Version `0.2.0-beta.1` changes the Dispatcharr plugin identity. Existing test installations must disable the old plugin, move `/data/plugins/dispatcharr_vod_newznab` to `/data/plugins/arr_stack_connector`, move `/data/dispatcharr_vod_newznab` to `/data/arr_stack_connector`, and copy the old plugin settings into the renamed plugin record. Do not enable both identities at once because both use port `9192` by default.
