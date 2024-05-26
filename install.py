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
	is_windows = True

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
	is_windows = False

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
EXTRAS_DIR = f"{ADWAITA_DIR}/extras"

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"
TARGET_WINDOWS = "C:\\Program Files (x86)\\Steam"

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
extrasdir = Path(EXTRAS_DIR)

# CSS List for @import
LIBRARY_FILES = [
	"css/_root/colors.css",
	"css/_root/icons.css",
	"css/_root/localization.css",
	"css/_root/opacity.css",
	"css/_root/text.css",
	"css/_root/variables.css",

	"css/widgets/avatars.css",
	"css/widgets/buttons.css",
	"css/widgets/cards.css",
	"css/widgets/checkboxes.css",
	"css/widgets/dialogs.css",
	"css/widgets/entries.css",
	"css/widgets/lists.css",
	"css/widgets/popups.css",
	"css/widgets/scrollbars.css",
	"css/widgets/windows.css",

	"css/main/headerbar/buttons.css",
	"css/main/headerbar/headerbar.css",
	"css/main/headerbar/menu.css",
	"css/main/headerbar/navigation.css",

	"css/main/library/details/header.css",
	"css/main/library/details/activity.css",
	"css/main/library/details/details.css",
	"css/main/library/details/event-dialog.css",

	"css/main/library/home/game-card.css",
	"css/main/library/home/home.css",
	"css/main/library/home/news.css",

	"css/main/library/sidebar/gamelist.css",
	"css/main/library/sidebar/sidebar.css",

	"css/main/library/library.css",

	"css/chat/chat.css",

	"css/dialogs/pagedsettings/dialog.css",
	"css/dialogs/pagedsettings/rows.css",

	"css/dialogs/login.css",
	"css/dialogs/settings.css",
	"css/dialogs/appproperties.css"
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
def patch_client_css(target: Path, name: str):
	print(f"{TEXT_BLUE}{TEXT_ARROW} Patching Steam Client {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE} Files...{TEXT_RESET}")

	if name == "Library":
		target_css = target / STEAM_LIBRARY_CSS
		orig_css = target / STEAM_ORIG_LIBRARY
		custom_library = target / STEAM_CUSTOM_LIBRARY
		custom_library_name = custom_library.name
	else:
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Invalid steam css patch selected: {name}{TEXT_RESET}")

	if not target_css.exists():
		print(f"{TEXT_PURPLE}{TEXT_INFO} File {TEXT_BOLD}{target_css}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
		return

	# Skip if already patched
	with target_css.open() as css_file:
		if css_file.readline().strip() == STEAM_PATCHED_HEADER:
			return

	orig_css = target_css.replace(target_css.with_suffix(".original.css"))
	name = target_css.stem
	css_dir = "css"

	content = f'{STEAM_PATCHED_HEADER}\n'
	content += format_import(STEAM_LOOPBACK, f"{css_dir}/{name}.original.css")
	content += format_import(STEAM_LOOPBACK, f"{custom_library_name}")

	target_css.open('w').write(content)

	size_diff = orig_css.stat().st_size - target_css.stat().st_size
	padding = " " * size_diff
	target_css.open('a').write(padding)

def uninstall_theme(target: Path):
	adwaita = target / STEAM_ADWAITA_DIR
	custom_library = target / STEAM_CUSTOM_LIBRARY
	steamui = target / STEAM_UI_DIR

	print(f"{TEXT_BLUE}{TEXT_ARROW} Uninstalling, resetting patched Steam CSS...{TEXT_RESET}")

	if not steamui.is_dir():
		print(f"{TEXT_PURPLE}{TEXT_INFO} steamui in {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_PURPLE} not found, skipping...{TEXT_RESET}")
		return

	open(custom_library, 'w').close()
	if adwaita.is_dir():
		shutil.rmtree(adwaita)

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
	parser.add_argument("-l", "--list-options", action = "store_true", help = "List available themes & extras and exit")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-u", "--uninstall", action = "store_true", help = "Uninstall theme")
	args = parser.parse_args()

	if args.target is None:
		args.target = ["normal", "flatpak"]

		if is_windows:
			args.target = ["windows"]			

	if args.list_options:
		list_options("color themes", find_color_themes(), ".css", colorthemedir, "color-theme")
		list_options("extras", find_extras(), ".css", extrasdir, "extras")
		exit(0)

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
		libraryroot = tmp / LIBRARY_ROOT_CSS

		print(f"{TEXT_BLUE}{TEXT_ARROW} Creating stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")

		generate_libraryroot(libraryroot, args.extras, selected_theme, args.custom_css)

		targets = set()

		for t in args.target:
			if t == "normal":
				targets.add(Path(TARGET_NORMAL).expanduser().resolve())
			elif t == "flatpak":
				targets.add(Path(TARGET_FLATPAK).expanduser().resolve())
			elif t == "windows":
				try:
					import winreg
					reg_path = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\Valve\\Steam"), "InstallPath")[0]
					targets.add(Path(reg_path).resolve())
				except:
					targets.add(Path(TARGET_WINDOWS).resolve())
			else:
				targets.add(Path(t).expanduser().resolve())

		for target in targets:
			if not target.is_dir():
				print(f"{TEXT_PURPLE}{TEXT_INFO} Directory {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
				continue

			if args.uninstall:
				uninstall_theme(target)
				continue

			patch_client_css(target, "Library")
			copy_dir(sourcedir, target / STEAM_ADWAITA_DIR)
			shutil.copy(libraryroot, target / STEAM_CUSTOM_LIBRARY)
			dev_reload(target)

		print(f"{TEXT_GREEN}{TEXT_CHECK} Done!{TEXT_RESET}")
