# Adwaita for Steam

A skin to make Steam look more like a native GNOME app

<p align="center">
	<img alt="Dark" src="/screenshots/dark.png" width="45%">
	&nbsp; &nbsp; &nbsp; &nbsp;
	<img alt="Light" src="/screenshots/light.png" width="45%">
</p>

### Limitations

* **Steam updates may reset theme**: The installer will patch Steam files in order to theme the interface, these files may be reset by Steam updates. When this happens, you will need to reinstall to repatch them.
* **Rounded corners**: Not all elements can be rounded, use [Rounded Window Corners Reborn extension](https://github.com/flexagoon/rounded-window-corners) on GNOME.
* **Steam website pages (Store/Community/Profiles/etc)**: No longer themable with the primary method.

## Color themes

<details><summary>Color theme previews</summary>

<table>
	<tr>
		<td><img alt="adwaita" src="/adwaita/colorthemes/adwaita/preview.png"><br/>adwaita</td>
		<td><img alt="adwaita-gray" src="/adwaita/colorthemes/adwaita-gray/preview.png"><br/>adwaita-gray</td>
		<td><img alt="breeze" src="/adwaita/colorthemes/breeze/preview.png"><br/>breeze</td>
		<td><img alt="canta" src="/adwaita/colorthemes/canta/preview.png"><br/>canta</td>
	</tr>
	<tr>
		<td><img alt="catppuccin-frappe" src="/adwaita/colorthemes/catppuccin-frappe/preview.png"><br/>catppuccin-frappe</td>
		<td><img alt="catppuccin-latte" src="/adwaita/colorthemes/catppuccin-latte/preview.png"><br/>catppuccin-latte</td>
		<td><img alt="catppuccin-macchiato" src="/adwaita/colorthemes/catppuccin-macchiato/preview.png"><br/>catppuccin-macchiato</td>
		<td><img alt="catppuccin-mocha" src="/adwaita/colorthemes/catppuccin-mocha/preview.png"><br/>catppuccin-mocha</td>
	</tr>
	<tr>
		<td><img alt="dracula" src="/adwaita/colorthemes/dracula/preview.png"><br/>dracula</td>
		<td><img alt="everforest" src="/adwaita/colorthemes/everforest/preview.png"><br/>everforest</td>
		<td><img alt="gruvbox" src="/adwaita/colorthemes/gruvbox/preview.png"><br/>gruvbox</td>
		<td><img alt="kate" src="/adwaita/colorthemes/kate/preview.png"><br/>kate</td>
	</tr>
	<tr>
		<td><img alt="metro" src="/adwaita/colorthemes/metro/preview.png"><br/>metro</td>
		<td><img alt="nord" src="/adwaita/colorthemes/nord/preview.png"><br/>nord</td>
		<td><img alt="oled" src="/adwaita/colorthemes/oled/preview.png"><br/>oled</td>
		<td><img alt="one-dark" src="/adwaita/colorthemes/one-dark/preview.png"><br/>one-dark</td>
	</tr>
	<tr>
		<td><img alt="pop" src="/adwaita/colorthemes/pop/preview.png"><br/>pop</td>
		<td><img alt="rose-pine" src="/adwaita/colorthemes/rose-pine/preview.png"><br/>rose-pine</td>
		<td><img alt="tokyo-night" src="/adwaita/colorthemes/tokyo-night/preview.png"><br/>tokyo-night</td>
		<td><img alt="tomorrow-night" src="/adwaita/colorthemes/tomorrow-night/preview.png"><br/>tomorrow-night</td>
	</tr>
	<tr>
		<td><img alt="vapor" src="/adwaita/colorthemes/vapor/preview.png"><br/>vapor</td>
		<td><img alt="vgui2" src="/adwaita/colorthemes/vgui2/preview.png"><br/>vgui2</td>
		<td><img alt="yaru" src="/adwaita/colorthemes/yaru/preview.png"><br/>yaru</td>
		<td></td>
	</tr>
</table>

</details>

## Installation

Adwaita-for-Steam supports multiple installation methods:
* [Installer script](#installer-script) - primary installation method, does not require any third-party CSS injectors.
* [AdwSteamGtk](#adwsteamgtk) (Linux, flatpak) - graphical application to configure installation options and automatically install skin updates.
* [Millennium](#millennium) - open-source modding framework for creating and managing Steam Client themes and plugins.
* [CSSLoader](#cssloader) - a native standalone styling engine for Steam on Windows and Linux.
* [SFP](#sfp) - skin and script injector for Steam (formerly SteamFriendsPatcher).

The installer script or `AdwSteamGtk` are the recommended installation methods.
Third-party injector support is provided for users who already use one of them.

Supported platforms:

| Platform | Installer script | AdwSteamGtk | Millennium | CSSLoader | SFP |
| --- | :-: | :-: | :-: | :-: | :-: |
| Linux, SteamOS | ✅ | ✅ | ✅ | ✅ | ✅ |
| Windows | ✅ | ❌ | ✅ | ✅ | ✅ |
| macOS | ✅ | ❌ | ❌ | ❌ | ✅ |

All installation methods except SFP support most of the available customization options:

| Platform | Installer script | AdwSteamGtk | Millennium | CSSLoader | SFP |
| --- | :-: | :-: | :-: | :-: | :-: |
| Color themes | ✅ | ✅ | ✅ | ✅ | Base theme only |
| Light/Dark mode | ✅ | ✅ | ✅ | ✅ | System only |
| Accent colors | ✅ | ✅ | ✅ | ✅ | Theme default |
| Window controls | ✅ | ✅ | ✅ | ✅ | Theme default |
| Extras | ✅ | ✅ | ✅ | ✅ | ❌ |
| Automatic updates | ❌ | ✅ | ✅ |   | ❌ |

### Installer script

```bash
git clone https://github.com/tkashkin/Adwaita-for-Steam
cd Adwaita-for-Steam
./install.py
```

#### Arguments

| Option                    | Short | Values                                                                                                                                | Default   | Description                                                                                                              |
| ------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------ |
| `--target`                | `-t`  | `default`, `flatpak`, `snap`, or a Steam installation path                                                                            | `default` | Install the skin to the selected Steam directories.                                                                      |
| `--color-theme`           | `-c`  | Available themes (see `--list-options`)                                                                                               | `adwaita` | Select the overall color palette.                                                                                        |
| `--color-scheme`          | `-s`  | `auto`, `light`, `dark`                                                                                                               | `auto`    | Follow the system appearance or force a light or dark theme.                                                             |
| `--accent-color`          | `-a`  | `auto`, `theme`<br/>Predefined color - `blue`, `teal`, `green`, `yellow`, `orange`, `red`, `pink`, `purple`, `slate`<br/>Custom color | `auto`    | Choose an accent color.<br/>`auto` uses the system accent when supported.<br/>`theme` uses the selected theme's default. |
| `--font`                  | `-f`  | `adwaita`, `cantarell`, `system`                                                                                                      | `adwaita` | Select the UI font.                                                                                                      |
| `--windowcontrols-theme`  |       | `auto`, `adwaita`, `breeze`, `windows`, `macos`                                                                                       | `auto`    | Choose the style of the window control buttons.                                                                          |
| `--windowcontrols-layout` |       | `auto`, `gnome`, `pantheon`, `kde`, `windows`, `macos`, or a custom layout string                                                     | `auto`    | Choose the button placement.<br/>Custom layouts use the GNOME format, e.g. `close,minimize:maximize`.                    |
| `--extra`                 | `-e`  | One or more extras (see `--list-options`)                                                                                             | None      | Enable optional tweaks such as UI customizations.                                                                        |
| `--custom-css`            |       | Path to a CSS file                                                                                                                    | None      | Load additional user CSS after the theme.                                                                                |
| `--no-optimize`           |       |                                                                                                                                       | Disabled  | Skip CSS bundling and minification (useful for development).                                                             |
| `--uninstall`             |       |                                                                                                                                       | Disabled  | Remove the skin from the selected Steam directories.                                                                     |


Examples:

```bash
# Show help
./install.py -h
# List color themes and extras
./install.py -l
# Install with customizations
./install.py -c catppuccin-macchiato -e login/hide-qr -e library/hide-whats-new
# Install with a color theme and a custom CSS file
./install.py -c catppuccin-macchiato --custom-css /path/to/custom.css
```

### AdwSteamGtk

[Graphical installer](https://github.com/Foldex/AdwSteamGtk) by [@Foldex](https://github.com/Foldex). Linux only. Supports automatic skin updates.

<a href="https://flathub.org/apps/details/io.github.Foldex.AdwSteamGtk"><img width="200" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-i-en.svg"/></a>

### Millennium

* Install [Millennium](https://steambrew.app).
* Copy Theme ID from the [theme page](https://steambrew.app/theme/7dzdgNotKWgNmQYXc6A0).
* Open Millennium Settings > Themes. Click "Install a theme" and paste the Theme ID.
* Enable the theme in Millennium.

### CSSLoader

* Install [CSSLoader-Desktop](https://github.com/DeckThemes/CSSLoader-Desktop) or the `CSSLoader` plugin for [Decky Loader](https://decky.xyz).
* Download the [latest Adwaita-for-Steam release](https://github.com/tkashkin/Adwaita-for-Steam/releases).
* Extract files to `~/homebrew/themes/Adwaita`.
* Enable the theme in CSSLoader.

### SFP

* Install [SFP](https://github.com/PhantomGamers/SFP).
* Download the [latest Adwaita-for-Steam release](https://github.com/tkashkin/Adwaita-for-Steam/releases).
* Extract files to `<Steam directory>/steamui/skins/Adwaita`.
* Enable the theme in SFP.