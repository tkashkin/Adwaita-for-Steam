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

### Adwaita

![Adwaita](/adwaita/colorthemes/adwaita/preview.png?raw=true)

### Breeze

![Breeze](/adwaita/colorthemes/breeze/preview.png?raw=true)

### Canta

![Canta](/adwaita/colorthemes/canta/preview.png?raw=true)

### Catppuccin-Frappe

![Catppuccin-Frappe](/adwaita/colorthemes/catppuccin-frappe/preview.png?raw=true)

### Catppuccin-Macchiato

![Catppuccin-Macchiato](/adwaita/colorthemes/catppuccin-macchiato/preview.png?raw=true)

### Catppuccin-Mocha

![Catppuccin-Mocha](/adwaita/colorthemes/catppuccin-mocha/preview.png?raw=true)

### Dracula

![Dracula](/adwaita/colorthemes/dracula/preview.png?raw=true)

### Everforest

![Everforest](/adwaita/colorthemes/everforest/preview.png?raw=true)

### Gruvbox

![Gruvbox](/adwaita/colorthemes/gruvbox/preview.png?raw=true)

### Kate

![Kate](/adwaita/colorthemes/kate/preview.png?raw=true)

### Metro

![Metro](/adwaita/colorthemes/metro/preview.png?raw=true)

### Nord

![Nord](/adwaita/colorthemes/nord/preview.png?raw=true)

### One Pro

![One Pro](/adwaita/colorthemes/one-pro/preview.png?raw=true)

### Pop

![Pop](/adwaita/colorthemes/pop/preview.png?raw=true)

### Tokyo Night

![Tokyo Night](/adwaita/colorthemes/tokyo-night/preview.png?raw=true)

### Tomorrow Night

![Tomorrow Night](/adwaita/colorthemes/tomorrow-night/preview.png?raw=true)

### Vapor

![Vapor](/adwaita/colorthemes/vapor/preview.png?raw=true)

### VGUI2

![VGUI2](/adwaita/colorthemes/vgui2/preview.png?raw=true)

### Yaru

![Yaru](/adwaita/colorthemes/yaru/preview.png?raw=true)

</details>

## Installation

### With installer script

```bash
git clone https://github.com/tkashkin/Adwaita-for-Steam
cd Adwaita-for-Steam
./install.py
```

#### Arguments

| Argument                | Short | Required Values                                       | Description                                        |
|-------------------------|-------|-------------------------------------------------------|----------------------------------------------------|
| --help                  | -h    |                                                       | Show help message                                  |
| --list-options          | -l    |                                                       | List available themes and extras                   |
| --color-theme           | -c    | [Colortheme](/adwaita/colorthemes)                    | Change color theme                                 |
| --windowcontrols-theme  |       | auto / adwaita / windows / macos                      | Change window control buttons style                |
| --windowcontrols-layout |       | auto / gnome / pantheon / windows / macos / \[custom] | Change window control buttons position and order   |
| --custom-css            |       |                                                       | Enable [custom css](/custom)                       |
| --extras                | -e    | [Extra](adwaita/extras)                               | Enable one or multiple theme extras                |
| --target                | -t    | normal / flatpak / \[custom dir]                      | Choose target location for install (default: both) |
| --uninstall             | -u    |                                                       | Uninstall theme                                    |

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

