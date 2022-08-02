# Adwaita for Steam

A skin to make Steam look more like a native GNOME app

<p align="center"><img src="screenshot.png?raw=true" /></p>

## Current state and plans

* **Main window**: mostly done, should be usable
* **Settings**: partially done
* **Common controls**: mostly done
* **High resolutions**: all new graphics assets have `@2x` variants that will be used when scaling is enabled in both Steam and OS settings
* **Small mode and other secondary windows**: planned if requested
* **Overlay**: unchanged, not planned
* **Old library, old chat, other old unused windows**: not planned
* **Recoloring**: colors can be changed in `Adwaita/adw/colors.styles`
* **Light theme**: not planned, would require redrawing all assets to be visible on light backgrounds

### Limitations

* **Rounded corners**: impossible to do in a Steam skin, use [mutter-rounded](https://github.com/yilozt/mutter-rounded) for GNOME or some other way to force rounded corners
* **Height of menu/sidebar items**: doesn't seem to be possible to increase
* **New library, new chat, other web-based client parts**: not skinnable without third-party tools, not planned as part of this project

## Requirements

* The skin was created for Linux version of Steam and wasn't tested on Windows or macOS. It will probably work with additional visual issues
* The skin uses [Cantarell](https://gitlab.gnome.org/GNOME/cantarell-fonts) as the default font, it may look broken without it

## Installation

1. Download the [latest skin version](https://github.com/tkashkin/Adwaita-for-Steam/archive/master.zip)
2. Extract `Adwaita` directory into Steam `skins` directory (create if it doesn't exist):
   * **Linux**: usually `~/.steam/steam/skins` or `~/.local/share/Steam/skins`
   * **Linux (flatpak)**: `~/.var/app/com.valvesoftware.Steam/.steam/steam/skins`
   * ~~Windows~~ (untested): `C:\Program Files (x86)\Steam\skins` by default
   * ~~macOS~~ (untested): `~/Library/Application Support/Steam/Steam.AppBundle/Steam/Contents/MacOS/skins`
3. Open Steam and select `Adwaita` skin in Settings > Interface (restart Steam if it doesn't appear in the list)
