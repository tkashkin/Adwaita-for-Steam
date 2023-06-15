# Adwaita for Steam

A skin to make Steam look more like a native GNOME app

<p align="center"><img src="screenshot.png?raw=true"/></p>

## Current state and plans

* **Main Window**: Done.
* **Login**: Done
* **Library**: Done
* **Small Mode**: Done.
* **Chat**: Done
* **Settings**: Mostly done.
* **New Overlay**: Mostly done.
* **New Big Picture**: Not done.
* **Recoloring**: Colors can be changed via making a new theme. See [colorthemes](colorthemes) dir.
* **Light Themes**: Not currently planned, though may now be more feasible with the new UI.

### Limitations

* **Steam updates may reset theme**: While the installer will patch steam files in order to theme the interface, these files may be reset by steam updates. If this happens, you will need to reinstall to repatch them.
* **Rounded corners**: Not all elements can be rounded, use [Rounded Window Corners extension](https://github.com/yilozt/rounded-window-corners) or [mutter-rounded](https://github.com/yilozt/mutter-rounded) on GNOME.
* **Steam website pages (Store/Community/Profiles/Etc)**: No longer themable with our current method.
* **Position of notifications**: Doesn't seem to be possible to change.
* **Height of sidebar items**: Doesn't seem to be possible to increase.

## Requirements

* [Cantarell fonts](https://gitlab.gnome.org/GNOME/cantarell-fonts): An option to install these is included in the install script, but fonts packaged by your distro are preferred.
* The skin was created for the Linux version of Steam and wasn't tested on Windows or macOS. It will work with some visual problems.

## Previews

<details><summary>Previews</summary>

### Adwaita

![Adwaita](/colorthemes/adwaita/preview.png?raw=true)

### Breeze

![Breeze](/colorthemes/breeze/preview.png?raw=true)

### Catppuccin-Frappe

![Catppuccin-Frappe](/colorthemes/catppuccin-frappe/preview.png?raw=true)

### Catppuccin-Macchiato

![Catppuccin-Macchiato](/colorthemes/catppuccin-macchiato/preview.png?raw=true)

### Catppuccin-Mocha

![Catppuccin-Mocha](/colorthemes/catppuccin-mocha/preview.png?raw=true)

### Dracula

![Dracula](/colorthemes/dracula/preview.png?raw=true)

### Gruvbox

![Gruvbox](/colorthemes/gruvbox/preview.png?raw=true)

### Kate

![Kate](/colorthemes/kate/preview.png?raw=true)

### Nord

![Nord](/colorthemes/nord/preview.png?raw=true)

### One Pro

![One Pro](/colorthemes/one-pro/preview.png?raw=true)

### Pop

![Pop](/colorthemes/pop/preview.png?raw=true)

### Tokyo Night

![Tokyo Night](/colorthemes/tokyo-night/preview.png?raw=true)

### Tomorrow Night

![Tomorrow Night](/colorthemes/tomorrow-night/preview.png?raw=true)

### Yaru

![Yaru](/colorthemes/yaru/preview.png?raw=true)

</details>

## Installation

### With installer script

```bash
git clone https://github.com/tkashkin/Adwaita-for-Steam
cd Adwaita-for-Steam
./install.py
```

#### Arguments

| Argument         | Short  | Required Values                  | Description                                              |
| ---------------- | ------ | -------------------------------- | -------------------------------------------------------- |
| --color-theme    | -c     | [Colortheme](colorthemes)        | Change color theme                                       |
| --font-install   | -fi    |                                  | Installs static Cantarell fonts                          |
| --list-options   | -l     |                                  | List available patches, themes, and web extras           |
| --target         | -t     | normal / flatpak / [custom dir]  | Choose target location for install (default: both)       |
| --uninstall      | -u     |                                  | Uninstall theme                                          |
| --web-theme      | -w     | full / base / none               | Choose web theme variant (default: full)                 |
| --web-extras     | -we    | [Web Extra](web/extras)          | Enable one or multiple web theme extras                  |

#### Example Usage

```bash
# List options
./install.py -l
# Install with options
./install.py -c nord -fi -p windowcontrols/right-all -we login/hide_qr -we library/hide_whats_new
```

### With graphical installer

Use the [graphical installer](https://github.com/Foldex/AdwSteamGtk) by [@Foldex](https://github.com/Foldex).

<a href="https://flathub.org/apps/details/io.github.Foldex.AdwSteamGtk"><img width="200" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-i-en.svg"/></a>

