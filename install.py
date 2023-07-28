#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from sys import platform
from tempfile import TemporaryDirectory, NamedTemporaryFile
from typing import NoReturn
import shutil
import time
import os

# Platform Specific
if platform == "win32":
	import winreg
	WINDOWS_RUN = True

	TEXT_BOLD = ""
	TEXT_BLUE = ""
	TEXT_GREEN = ""
	TEXT_PURPLE = ""
	TEXT_RED = ""
	TEXT_RESET = ""

	TEXT_ARROW = ""
	TEXT_CHECK = ""
	TEXT_CROSS = ""
	TEXT_INFO = ""
else:
	WINDOWS_RUN = False

	TEXT_BOLD = "\033[1m"
	TEXT_BLUE = "\033[1;34m"
	TEXT_GREEN = "\033[1;32m"
	TEXT_PURPLE = "\033[1;35m"
	TEXT_RED = "\033[1;31m"
	TEXT_RESET = "\033[0m"

	TEXT_ARROW = "→"
	TEXT_CHECK = "✓"
	TEXT_CROSS = "✖"
	TEXT_INFO = "✦"

ADWAITA_DIR = "adwaita"
COLOR_THEME_DIR = f"{ADWAITA_DIR}/colorthemes"
CUSTOM_DIR = "custom"
FONTS_DIR = "fonts"
EXTRAS_DIR = f"{ADWAITA_DIR}/extras"

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"
TARGET_WINDOWS = "C:/Program Files (x86)/Steam"

TARGET_FONTS = "~/.local/share/fonts"
TARGET_FONTS_WIN = "AppData/Local/Microsoft/Windows/Fonts"

STEAM_LOOPBACK = "https://steamloopback.host"
STEAM_LOOPBACK_ADWAITA = f"{STEAM_LOOPBACK}/{ADWAITA_DIR}"
STEAM_PATCHED_HEADER = "/*patched*/"

STEAM_UI_DIR = "steamui"
STEAM_ADWAITA_DIR = f"{STEAM_UI_DIR}/{ADWAITA_DIR}"
STEAM_CSS_DIR = f"{STEAM_UI_DIR}/css"

STEAM_LIBRARY_CSS = f"{STEAM_CSS_DIR}/library.css"
STEAM_ORIG_LIBRARY = f"{STEAM_CSS_DIR}/library.original.css"
STEAM_CUSTOM_LIBRARY = f"{STEAM_UI_DIR}/libraryroot.custom.css"

LIBRARY_ROOT_CSS = "libraryroot.custom.css"
CUSTOM_CSS = "custom.css"


adwaitadir = Path(ADWAITA_DIR)
colorthemedir = Path(COLOR_THEME_DIR)
customdir = Path(CUSTOM_DIR)
fontdir = Path(FONTS_DIR)
extrasdir = Path(EXTRAS_DIR)

# CSS List for @import
LIBRARY_FILES = [
	# General
	"variants/base/_root.css",
	"variants/base/_localization.css",
	"variants/base/scrollbars.css",
	# Main window
	"variants/base/main_window/headerbar/headerbar.css",
	"variants/base/main_window/headerbar/buttons.css",
	"variants/base/main_window/headerbar/navigation.css",
	"variants/base/main_window/headerbar/menu.css",
	# Library
	"variants/base/library.css",
	"variants/full/library.css",
	"variants/base/game_details.css",
	"variants/full/game_details.css",
	"variants/base/downloads.css",
	"variants/full/downloads.css",
	"variants/base/collections.css",
	# Dialogs
	"variants/base/dialogs/_dialogs.css",
	"variants/base/dialogs/launch_options.css",
	"variants/base/dialogs/login.css",
	"variants/full/dialogs/_dialogs.css",
	"variants/full/dialogs/about_steam.css",
	"variants/full/dialogs/add_game.css",
	"variants/full/dialogs/app_properties.css",
	"variants/full/dialogs/content_management.css",
	"variants/full/dialogs/install_game.css",
	"variants/full/dialogs/paged_settings.css",
	"variants/full/dialogs/product_activation.css",
	"variants/full/dialogs/recent_players.css",
	"variants/full/dialogs/screenshots.css",
	"variants/full/dialogs/server_browser.css",
	"variants/full/dialogs/steam_settings.css",
	"variants/full/dialogs/system_information.css",
	"variants/full/dialogs/uninstall.css",
	"variants/full/dialogs/whats_new.css",
	# In-Game Overlay
	"variants/base/game_overlay.css",
	# Notifications
	"variants/base/notifications.css",
	# Chat
	"variants/full/chat.css",
]


# Utils
def copy_dir(source: Path, target: Path):
	if not source.is_dir():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} copy_dir:{source} is not a valid directory.{TEXT_RESET}")
	if target.is_dir():
		shutil.rmtree(target)
	shutil.copytree(source, target)

# List Options
def list_options(type: str, options: list[Path], suffix: str, sourcedir: Path, arg: str):
	if options:
		print(f"{TEXT_BLUE}{TEXT_BOLD}{type.upper()}: {len(options)}{TEXT_RESET}")
		for option in options:
			name = os.path.relpath(option, sourcedir).removesuffix(suffix).replace("\\", "/")

			if type == "color themes":
				name = name.split("/")[1]

			description = ""

			print(f"{TEXT_PURPLE}{TEXT_BOLD}{name}{TEXT_RESET}{description}")
		print(f"\nApply {type} using {TEXT_GREEN}'./install.py --{arg} NAME'{TEXT_RESET}\n")
	else:
		print(f"{TEXT_PURPLE}{TEXT_INFO} No {type} available\n{TEXT_RESET}")

# Fonts
def install_font(name: str):
	if WINDOWS_RUN:
		target = Path.home() / TARGET_FONTS_WIN
		ext = "ttf"
	else:
		target = Path(TARGET_FONTS).expanduser().resolve()
		ext = "otf"

	font = fontdir / name / ext

	if not font.is_dir():
		print(f"{TEXT_PURPLE}{TEXT_INFO} Font: {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_PURPLE} not found!{TEXT_RESET}")
		return

	print(f"\n{TEXT_BLUE}{TEXT_ARROW} Installing font {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
	files = font.glob(f"*.{ext}")
	target.mkdir(exist_ok = True)
	for f in files:
		target_file = target / f.name

		if target_file.is_file():
			print(f"  {TEXT_BLUE}{TEXT_ARROW} Font {TEXT_BOLD}{f.name}{TEXT_RESET}{TEXT_BLUE} exists. Skipping...{TEXT_RESET}")
			continue

		shutil.copy(f, target)
		if WINDOWS_RUN:
			win_reg_font(f.name, target_file)

def win_reg_font(name: str, target: Path):
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 0, winreg.KEY_ALL_ACCESS)
	winreg.SetValueEx(key, str(name), 0, winreg.REG_SZ, str(target))
	winreg.CloseKey(key)

# CSS Theme
def find_extras() -> list[Path]:
	return list(extrasdir.glob("**/*.css"))

def format_import(prefix: str, string: str) -> str:
	return f"@import url(\"{prefix}/{string}\");\n"

def generate_libraryroot(target: Path, selected_extras: list[Path], selected_theme: str, custom_css: bool):
	content = "/* Main Files */\n"
	for f in LIBRARY_FILES:
		content += format_import(STEAM_LOOPBACK_ADWAITA, f)

	if selected_extras:
		print()
		content += "\n/* Extras */\n"

		for extra in selected_extras:
			we = extra.removesuffix(".css")
			test = extrasdir / we
			if test.with_suffix(".css").exists():
				print(f"{TEXT_BLUE}{TEXT_ARROW} Applying extra {TEXT_BOLD}{we}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
				content += format_import(STEAM_LOOPBACK_ADWAITA, f"extras/{we}.css")
			else:
				print(f"{TEXT_PURPLE}{TEXT_INFO} Extra: {TEXT_BOLD}{we}{TEXT_RESET}{TEXT_PURPLE} not found!{TEXT_RESET}")
		print()

	if selected_theme:
		print(f"{TEXT_BLUE}{TEXT_ARROW} Applying color theme {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}\n")
		content += "\n/* ColorTheme */\n"
		content += format_import(STEAM_LOOPBACK_ADWAITA, f"colorthemes/{selected_theme}/{selected_theme}.css")

	if custom_css:
		print(f"{TEXT_BLUE}{TEXT_ARROW} Applying custom css...{TEXT_RESET}\n")
		content += "\n/* Custom CSS */\n"
		content += format_import(STEAM_LOOPBACK_ADWAITA, f"custom/{CUSTOM_CSS}")

	target.open('w').write(content)

# Color Themes
def find_color_themes() -> list[Path]:
	return list(sorted(colorthemedir.glob("**/*.css")))

# Patching
def patch_client_css(source: Path, target: Path, name: str):
	print(f"{TEXT_BLUE}{TEXT_ARROW} Patching Steam Client {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE} Files...{TEXT_RESET}")

	if name == "Library":
		target_adwaita = target / STEAM_ADWAITA_DIR
		target_css = target / STEAM_LIBRARY_CSS
		orig_css = target / STEAM_ORIG_LIBRARY
		custom_library = target / STEAM_CUSTOM_LIBRARY
		custom_library_name = custom_library.name
		source_css = source / LIBRARY_ROOT_CSS
	else:
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Invalid steam css patch selected: {name}{TEXT_RESET}")

	if not target_css.exists():
		print(f"{TEXT_PURPLE}{TEXT_INFO} File {TEXT_BOLD}{target_css}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
		return

	if args.uninstall:
		print(f"{TEXT_BLUE}{TEXT_ARROW} Uninstalling, resetting patched Steam {name} CSS...{TEXT_RESET}")
		open(custom_library, 'w').close()
		if target_adwaita.is_dir():
			shutil.rmtree(target_adwaita)
	else:
		shutil.move(source_css, custom_library)

	# Skip if already patched
	with target_css.open() as css_file:
		if css_file.readline().strip() == STEAM_PATCHED_HEADER:
			return

	orig_css = target_css.rename(target_css.with_suffix(".original.css"))
	name = target_css.stem
	css_dir = "css"

	content = f'{STEAM_PATCHED_HEADER}\n'
	content += format_import(STEAM_LOOPBACK, f"{css_dir}/{name}.original.css")
	content += format_import(STEAM_LOOPBACK, f"{custom_library_name}")

	target_css.open('w').write(content)

	size_diff = orig_css.stat().st_size - target_css.stat().st_size
	padding = " " * size_diff
	target_css.open('a').write(padding)

# It is possible to force the steam client to reload the theme by creating a uniquely named new file inside the steamui dir.
# This only seems to work when Steam is run with the -dev arg, and reloading repeatedly can leak a lot of memory.
# Still, this is useful for testing changes
def dev_reload(target: Path):
	if not args.dev or not target.is_dir():
		return

	sd = target / "steamui"
	if not sd.is_dir():
		print("{TEXT_PURPLE}steamui dir not found. Cannot hot reload.{TEXT_RESET}")
		return

	with NamedTemporaryFile(dir=sd) as tmpfile:
		tmpfile.write(b"")
		time.sleep(3)

# Run
if __name__ == "__main__":
	if not adwaitadir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Theme directory {TEXT_BOLD}{ADWAITA_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")
	if not colorthemedir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Color Theme directory {TEXT_BOLD}{COLOR_THEME_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")

	parser = ArgumentParser(description = "Adwaita-for-Steam installer")
	parser.add_argument("-c", "--color-theme", default = "adwaita", help = "Choose color theme")
	parser.add_argument("--custom-css", action = "store_true", help = "Enable Custom CSS")
	parser.add_argument("-d", "--dev", action = "store_true", help = "Dev Mode")
	parser.add_argument("-e", "--extras", nargs = "+", action = "extend", help = "Enable one or multiple theme extras")
	parser.add_argument("-f", "--font-install", action = "store_true", help = "Install Fonts")
	parser.add_argument("-l", "--list-options", action = "store_true", help = "List available themes & extras and exit")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", default = ["normal", "flatpak"], help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-u", "--uninstall", action = "store_true", help = "Uninstall theme")
	parser.add_argument("-w", "--web-theme", choices = ["base", "full"], default = "full", help = "Deprecated, does nothing.") # Keeping for compatability
	args = parser.parse_args()

	if WINDOWS_RUN:
		args.target = ["windows"]

	if args.list_options:
		list_options("color themes", find_color_themes(), ".css", colorthemedir, "color-theme")
		list_options("extras", find_extras(), ".css", extrasdir, "extras")
		exit(0)

	if args.font_install:
		install_font("Cantarell")

	selected_theme = None
	if args.color_theme:

		if args.color_theme == "adwaita":
			selected_theme = None
		else:
			t = args.color_theme.removesuffix(".css")
			selected_theme = t
			test = colorthemedir / t / t
			if not test.with_suffix(".css").exists():
				raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} {TEXT_BOLD}{test}{TEXT_RESET}{TEXT_RED} theme not found.{TEXT_RESET}")


	with TemporaryDirectory() as tmpdir:
		tmp = Path(tmpdir)

		copy_dir(adwaitadir, tmp / ADWAITA_DIR)
		copy_dir(customdir, tmp / ADWAITA_DIR / CUSTOM_DIR)
		sourcedir = tmp / ADWAITA_DIR

		print(f"{TEXT_BLUE}{TEXT_ARROW} Creating stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")

		generate_libraryroot(sourcedir / LIBRARY_ROOT_CSS, args.extras, selected_theme, args.custom_css)

		targets = set()

		for t in args.target:
			if t == "normal":
				targets.add(Path(TARGET_NORMAL).expanduser().resolve())
			elif t == "flatpak":
				targets.add(Path(TARGET_FLATPAK).expanduser().resolve())
			elif t == "windows":
				targets.add(Path(TARGET_WINDOWS))
			else:
				targets.add(Path(t).expanduser().resolve())

		for target in targets:
			if not target.is_dir():
				print(f"{TEXT_PURPLE}{TEXT_INFO} Directory {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
				continue

			patch_client_css(sourcedir, target, "Library")

			if not args.uninstall:
				copy_dir(sourcedir, target / STEAM_ADWAITA_DIR)
				dev_reload(target)

		print(f"{TEXT_GREEN}{TEXT_CHECK} Done!{TEXT_RESET}")
