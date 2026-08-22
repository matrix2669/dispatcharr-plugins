# Dispatcharr Plugins

Third-party Dispatcharr plugin registries maintained by matrix2669.

Each plugin remains in its own source repository. This repository contains only the channel manifests and per-plugin publication metadata that tell Dispatcharr which immutable plugin build to install.

## Stable channel

Use the stable registry for plugins with an explicitly approved GitHub Release:

```text
https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/main/manifest.json
```

The `main` branch never advertises a plugin merely because a tag exists. A plugin enters this channel only after its stable release has been approved and published.

## Tagged-build channel

Use the `dev` registry for the newest tagged build of each plugin:

```text
https://raw.githubusercontent.com/matrix2669/dispatcharr-plugins/dev/manifest.json
```

During active testing, the newest tag may be a beta such as `1.2.0-beta.3`. After feature or fix work is completed, the entry advances to the completed stable tag such as `1.2.0`, even when that version has not been published as a GitHub Release. If no beta is active, the plugin remains on its latest completed stable tag rather than being removed from `dev`.

A completed stable version and a released version are different states. Tags in `dev` do not authorize publication to `main`.

When the newest tagged build is already the same released version advertised by `main`, the `dev` index may reuse that `main` per-plugin manifest. A separate `dev` per-plugin manifest is needed only when `dev` advertises a different beta or completed-but-unreleased stable tag.

Add the appropriate URL under **Plugins → Plugin Repositories**. Users who want only generally released plugins should configure only `main`.

## Repository scope

This repository does not package plugin code and does not publish releases or versions of its own. Plugin source repositories own their tags, releases, installable artifacts, and changelogs. See `RELEASE.md` for the registry publication procedure.
