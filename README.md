# Adwaita for Steam

A skin to make Steam look more like a native GNOME app

<p align="center">
	<img alt="Store" src="/screenshots/store.png?raw=true" width="45%">
	&nbsp; &nbsp; &nbsp; &nbsp;
	<img alt="Library" src="/screenshots/library.png?raw=true" width="45%">
</p>

### Limitations

* **Steam updates may reset theme**: While the installer will patch steam files in order to theme the interface, these files may be reset by steam updates. If this happens, you will need to reinstall to repatch them.
* **Rounded corners**: Not all elements can be rounded, use [Rounded Window Corners Reborn extension](https://github.com/flexagoon/rounded-window-corners) on GNOME.
* **Steam website pages (Store/Community/Profiles/etc)**: No longer themable with our current method.
* **Position of notifications**: Doesn't seem to be possible to change.
* **Height of game list entries**: Doesn't seem to be possible to increase.

## Requirements

* [Python 3](https://www.python.org/downloads/)
* The skin is created and tested mostly on the Linux version of Steam. Steam's new UI has largely unified platform differences, so other platforms should work, but are not a priority.

## Color themes

<details><summary>Color theme previews</summary>

<table>
	<tr>
		<td><img alt="adwaita" src="/adwaita/colorthemes/adwaita/preview.png?raw=true"><br/>adwaita</td>
		<td><img alt="breeze" src="/adwaita/colorthemes/breeze/preview.png?raw=true"><br/>breeze</td>
		<td><img alt="canta" src="/adwaita/colorthemes/canta/preview.png?raw=true"><br/>canta</td>
	</tr>
	<tr>
		<td><img alt="catppuccin-frappe" src="/adwaita/colorthemes/catppuccin-frappe/preview.png?raw=true"><br/>catppuccin-frappe</td>
		<td><img alt="catppuccin-macchiato" src="/adwaita/colorthemes/catppuccin-macchiato/preview.png?raw=true"><br/>catppuccin-macchiato</td>
		<td><img alt="catppuccin-mocha" src="/adwaita/colorthemes/catppuccin-mocha/preview.png?raw=true"><br/>catppuccin-mocha</td>
	</tr>
	<tr>
		<td><img alt="dracula" src="/adwaita/colorthemes/dracula/preview.png?raw=true"><br/>dracula</td>
		<td><img alt="everforest" src="/adwaita/colorthemes/everforest/preview.png?raw=true"><br/>everforest</td>
		<td><img alt="gruvbox" src="/adwaita/colorthemes/gruvbox/preview.png?raw=true"><br/>gruvbox</td>
	</tr>
	<tr>
		<td><img alt="kate" src="/adwaita/colorthemes/kate/preview.png?raw=true"><br/>kate</td>
		<td><img alt="metro" src="/adwaita/colorthemes/metro/preview.png?raw=true"><br/>metro</td>
		<td><img alt="nord" src="/adwaita/colorthemes/nord/preview.png?raw=true"><br/>nord</td>
	</tr>
	<tr>
		<td><img alt="oled" src="/adwaita/colorthemes/oled/preview.png?raw=true"><br/>oled</td>
		<td><img alt="one-pro" src="/adwaita/colorthemes/one-pro/preview.png?raw=true"><br/>one-pro</td>
		<td><img alt="pop" src="/adwaita/colorthemes/pop/preview.png?raw=true"><br/>pop</td>
	</tr>
	<tr>
		<td><img alt="rose-pine" src="/adwaita/colorthemes/rose-pine/preview.png?raw=true"><br/>rose-pine</td>
		<td><img alt="tokyo-night" src="/adwaita/colorthemes/tokyo-night/preview.png?raw=true"><br/>tokyo-night</td>
		<td><img alt="tomorrow-night" src="/adwaita/colorthemes/tomorrow-night/preview.png?raw=true"><br/>tomorrow-night</td>
	</tr>
	<tr>
		<td><img alt="vapor" src="/adwaita/colorthemes/vapor/preview.png?raw=true"><br/>vapor</td>
		<td><img alt="vgui2" src="/adwaita/colorthemes/vgui2/preview.png?raw=true"><br/>vgui2</td>
		<td><img alt="yaru" src="/adwaita/colorthemes/yaru/preview.png?raw=true"><br/>yaru</td>
	</tr>
</table>

</details>

## Installation

### With installer script

```bash
git clone https://github.com/tkashkin/Adwaita-for-Steam
cd Adwaita-for-Steam
./install.py
```

#### Arguments

| Argument                | Short | Required Values                                          | Description                                      |
|-------------------------|-------|----------------------------------------------------------|--------------------------------------------------|
| --help                  | -h    |                                                          | Show help message                                |
| --list-options          | -l    |                                                          | List available themes and extras                 |
| --color-theme           | -c    | [Colortheme](/adwaita/colorthemes)                       | Change color theme                               |
| --font                  | -f    | adwaita / cantarell                                      | Change font family                               |
| --windowcontrols-theme  |       | auto / adwaita / breeze / windows / macos                | Change window control buttons style              |
| --windowcontrols-layout |       | auto / gnome / pantheon / windows / macos / \[custom]    | Change window control buttons position and order |
| --custom-css            |       |                                                          | Enable [custom css](/custom)                     |
| --extras                | -e    | [Extra](adwaita/extras)                                  | Enable one or multiple theme extras              |
| --target                | -t    | linux / windows / macos / flatpak / snap / \[custom dir] | Choose target location for install               |
| --uninstall             | -u    |                                                          | Uninstall theme                                  |

#### Example Usage

```bash
# List options
./install.py -l
# Install with customizations
./install.py -c nord -e login/hide_qr -e library/hide_whats_new
```

<details><summary>Custom CSS</summary>

If you wish to include your own custom CSS, see [custom](/custom) and use the `--custom-css` flag.

```bash
./install.py --custom-css
```

</details>

### With graphical installer

Use the [graphical installer](https://github.com/Foldex/AdwSteamGtk) by [@Foldex](https://github.com/Foldex).

<a href="https://flathub.org/apps/details/io.github.Foldex.AdwSteamGtk"><img width="200" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-i-en.svg"/></a>

### Windows Install

- Download the [Latest Release](https://github.com/tkashkin/Adwaita-for-Steam/releases)
- Ensure you have [Python](#requirements) installed
- Double click the `install_windows` bat script and follow the prompts

