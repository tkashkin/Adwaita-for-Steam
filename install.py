#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile
from typing import NoReturn
import configparser
import re
import shutil
import time
import os

TEXT_BOLD = "\033[1m"
TEXT_BLUE = "\033[1;34m"
TEXT_GREEN = "\033[1;32m"
TEXT_PURPLE = "\033[1;35m"
TEXT_RED = "\033[1;31m"
TEXT_RESET = "\033[0m"

TEXT_ARROW="→"
TEXT_CHECK="✓"
TEXT_CROSS="✖"
TEXT_INFO="✦"

COLOR_THEME_DIR = "colorthemes"
FONTS_DIR = "fonts"
WEB_EXTRAS_DIR = "web/extras"
WEB_THEME_DIR = "web"

LIBRARY_CSS_FILE = "libraryroot.custom.css"

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"

TARGET_FONTS = "~/.local/share/fonts"

STEAM_LOOPBACK = "https://steamloopback.host"
STEAM_PATCHED_HEADER = "/*patched*/"

STEAM_FRIENDS_CSS = "clientui/css/friends.css"
STEAM_LIBRARY_CSS = "steamui/css/library.css"
STEAM_ORIG_LIBRARY = "steamui/css/library.original.css"
STEAM_ORIG_FRIENDS = "clientui/css/friends.original.css"
STEAM_CUSTOM_LIBRARY = "steamui/libraryroot.custom.css"
STEAM_CUSTOM_FRIENDS = "clientui/friends.custom.css"

colorthemedir = Path(COLOR_THEME_DIR)
fontdir = Path(FONTS_DIR)
webextrasdir = Path(WEB_EXTRAS_DIR)
webthemedir = Path(WEB_THEME_DIR)

# CSS for Steam Library Patching
LIBRARY_BASE_FILES = [
	# Web
	webthemedir / "base/_root.css",
	webthemedir / "base/scrollbars.css",
	# Header/Footer
	webthemedir / "base/top_bar.css",
	webthemedir / "base/bottom_bar.css",
	# In-Game Overlay
	webthemedir / "base/game_overlay.css",
	# Notifications
	webthemedir / "base/notifications.css",
	# Library
	webthemedir / "base/library.css",
	webthemedir / "base/game_details.css",
	webthemedir / "base/downloads.css",
	webthemedir / "base/collections.css",
	# Web Dialogs
	webthemedir / "base/dialogs/_dialogs.css",
	# Library Dialogs
	webthemedir / "base/dialogs/login.css",
	webthemedir / "base/dialogs/launch_options.css",
]

LIBRARY_FULL_FILES = [
	# Web
	webthemedir / "base/_root.css",
	webthemedir / "base/scrollbars.css",
	webthemedir / "full/chat.css",
	# Header/Footer
	webthemedir / "base/top_bar.css",
	webthemedir / "base/bottom_bar.css",
	# In-Game Overlay
	webthemedir / "base/game_overlay.css",
	# Notifications
	webthemedir / "base/notifications.css",
	# Library
	webthemedir / "base/library.css",
	webthemedir / "full/library.css",
	webthemedir / "base/game_details.css",
	webthemedir / "full/game_details.css",
	webthemedir / "base/downloads.css",
	webthemedir / "full/downloads.css",
	webthemedir / "base/collections.css",
	# Web Dialogs
	webthemedir / "base/dialogs/_dialogs.css",
	webthemedir / "full/dialogs/_dialogs.css",
	webthemedir / "full/dialogs/paged_settings.css",
	# Library Dialogs
	webthemedir / "base/dialogs/launch_options.css",
	webthemedir / "base/dialogs/login.css",
	webthemedir / "full/dialogs/about_steam.css",
	webthemedir / "full/dialogs/add_game.css",
	webthemedir / "full/dialogs/app_properties.css",
	webthemedir / "full/dialogs/content_management.css",
	webthemedir / "full/dialogs/install_game.css",
	webthemedir / "full/dialogs/product_activation.css",
	webthemedir / "full/dialogs/recent_players.css",
	webthemedir / "full/dialogs/screenshots.css",
	webthemedir / "full/dialogs/server_browser.css",
	webthemedir / "full/dialogs/steam_settings.css",
	webthemedir / "full/dialogs/system_information.css",
	webthemedir / "full/dialogs/uninstall.css",
	webthemedir / "full/dialogs/whats_new.css",
]

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
def install_font(name: str, ext: str):
	font = fontdir / name / ext
	if font.exists():
		print(f"\n{TEXT_BLUE}{TEXT_ARROW} Installing font {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
		files = font.glob(f"*.{ext}")
		target = Path(TARGET_FONTS).expanduser().resolve()
		target.mkdir(exist_ok = True)
		for f in files:
			shutil.copy(f, target)
	else:
		print(f"{TEXT_PURPLE}{TEXT_INFO} Font: {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_PURPLE} not found!{TEXT_RESET}")

# Webkit CSS
def find_web_extras() -> list[Path]:
	return list(webextrasdir.glob("**/*.css"))

def gen_webkit_theme(target: Path, name: str, selected_extras: list[Path]):
	if name == "none":
		return
	elif name == "library_base":
		selected_files = LIBRARY_BASE_FILES
	elif name == "library_full":
		selected_files = LIBRARY_FULL_FILES
	else:
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Invalid web theme selected: {name}{TEXT_RESET}")

	with open(target,'wb') as wfd:
		for f in selected_files:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd)

		if selected_extras:
			print()
			for f in selected_extras:
				we = f.removesuffix(".css")
				f = Path(f)

				if not f.exists() or f.suffix != ".css":
					f = webthemedir / "extras" / "{}{}".format(we, ".css")

				if f.exists():
					with open(f,'rb') as fd:
						print(f"{TEXT_BLUE}{TEXT_ARROW} Applying web_extra {TEXT_BOLD}{we}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
						shutil.copyfileobj(fd, wfd)
				else:
					print(f"{TEXT_PURPLE}{TEXT_INFO} Web Extra: {TEXT_BOLD}{f}{TEXT_RESET}{TEXT_PURPLE} not found!{TEXT_RESET}")
			print()

# Color Themes
def find_color_themes() -> list[Path]:
	return list(sorted(colorthemedir.glob("**/*.theme")))

def hex2css(name: str, hex: str) -> str:
	return f'--{name}: {hex};'

def replace_css_colors(target: Path, config: configparser.ConfigParser):
	if args.uninstall:
		return

	with open (target, 'r' ) as f:
		content = f.read()

	for section in config.sections():
		for (key, val) in config.items(section):
			s = hex2css(key, val)
			content = re.sub(f'^(\s+)--{key}: [^;]+;$', r'\1' + s, content, flags = re.M)

	with open (target, 'w' ) as f:
		f.write(content)

# Install
def install(source: Path, target: Path, name: str):
	if target.is_dir():
		if target.stem != "skins":
			target = target / "skins"
			target.mkdir(exist_ok = True)
	else:
		print(f"{TEXT_PURPLE}{TEXT_INFO} Directory {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
		return
	print(f"{TEXT_BLUE}{TEXT_ARROW} Installing skin {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE} into {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
	target_skin = target / name
	if target_skin.exists():
		shutil.rmtree(target_skin)
	shutil.copytree(source, target_skin)

def patch_client_css(source: Path, target: Path, name: str):
	if not target.is_dir():
		print(f"{TEXT_PURPLE}{TEXT_INFO} Directory {TEXT_BOLD}{target}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
		return

	print(f"{TEXT_BLUE}{TEXT_ARROW} Patching Steam Client {TEXT_BOLD}{name}{TEXT_RESET}{TEXT_BLUE} Files...{TEXT_RESET}")


	if name == "Library":
		target_css = target / STEAM_LIBRARY_CSS
		orig_css = target / STEAM_ORIG_LIBRARY
		custom_css = target / STEAM_CUSTOM_LIBRARY
		custom_css_name = custom_css.name
		source_css = source / LIBRARY_CSS_FILE
	# elif name == "Friends":
	# 	target_css = target / STEAM_FRIENDS_CSS
	# 	orig_css = target / STEAM_ORIG_FRIENDS
	# 	custom_css = target / STEAM_CUSTOM_FRIENDS
	# 	custom_css_name = custom_css.name
	# 	source_css = source / CSS_FILE
	else:
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Invalid steam css patch selected: {name}{TEXT_RESET}")

	if not target_css.exists():
		print(f"{TEXT_PURPLE}{TEXT_INFO} File {TEXT_BOLD}{target_css}{TEXT_RESET}{TEXT_PURPLE} does not exist{TEXT_RESET}")
		return

	if args.uninstall:
		print(f"{TEXT_BLUE}{TEXT_ARROW} Uninstalling, resetting patched Steam {name} CSS...{TEXT_RESET}")
		open(custom_css, 'w').close()
	else:
		shutil.copy(source_css, custom_css)

	with target_css.open() as css_file:
		if css_file.readline().strip() == STEAM_PATCHED_HEADER:
			return

	orig_css = target_css.rename(target_css.with_suffix(".original.css"))
	name = target_css.stem
	css_dir = "css"
	content = f'{STEAM_PATCHED_HEADER}\n@import url("{STEAM_LOOPBACK}/{css_dir}/{name}.original.css");\n@import url("{STEAM_LOOPBACK}/{custom_css_name}");\n'
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

if __name__ == "__main__":
	if not webthemedir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Web Theme directory {TEXT_BOLD}{WEB_THEME_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")
	if not colorthemedir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Color Theme directory {TEXT_BOLD}{COLOR_THEME_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")

	parser = ArgumentParser(description = "Adwaita-for-Steam installer")
	parser.add_argument("-c", "--color-theme", default = "adwaita", help = "Choose color theme")
	parser.add_argument("-d", "--dev", action = "store_true", help = "Dev Mode")
	parser.add_argument("-fi", "--font-install", action = "store_true", help = "Install Fonts")
	parser.add_argument("-l", "--list-options", action = "store_true", help = "List available themes & web extras and exit")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", default = ["normal", "flatpak"], help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-u", "--uninstall", action = "store_true", help = "Uninstall theme")
	parser.add_argument("-w", "--web-theme", choices = ["base", "full"], default = "full", help = "Choose web theme variant")
	parser.add_argument("-we", "--web-extras", nargs = "+", action = "extend", help = "Enable one or multiple web theme extras")
	args = parser.parse_args()

	if args.list_options:
		list_options("color themes", find_color_themes(), ".theme", colorthemedir, "color-theme")
		list_options("web extras", find_web_extras(), ".css", webextrasdir, "web-extras")
		exit(0)

	if args.font_install:
		install_font("Cantarell", "otf")

	selected_theme = None
	if args.color_theme:
		ct = Path(args.color_theme)

		if args.color_theme.removesuffix(".theme") == "adwaita":
			selected_theme = None
		elif ct.exists() and ct.suffix == ".theme":
			selected_theme = ct
		else:
			t = args.color_theme.removesuffix(".theme")
			selected_theme = colorthemedir / t / "{}{}".format(t, ".theme")
			if not selected_theme.exists():
				raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_RED} theme not found.{TEXT_RESET}")

	with TemporaryDirectory() as tmpdir:
		tmp = Path(tmpdir)
		sourcedir = tmp
		print(f"{TEXT_BLUE}{TEXT_ARROW} Creating stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")

		if args.web_theme == "full":
			gen_webkit_theme(sourcedir / LIBRARY_CSS_FILE, "library_full", args.web_extras)
		elif args.web_theme == "base":
			gen_webkit_theme(sourcedir / LIBRARY_CSS_FILE, "library_base", args.web_extras)

		if selected_theme:
			print(f"{TEXT_BLUE}{TEXT_ARROW} Applying color theme {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
			config = configparser.ConfigParser()
			config.read(selected_theme)
			replace_css_colors(sourcedir / LIBRARY_CSS_FILE, config)

		targets = set()

		for t in args.target:
			if t == "normal":
				targets.add(Path(TARGET_NORMAL).expanduser().resolve())
			elif t == "flatpak":
				targets.add(Path(TARGET_FLATPAK).expanduser().resolve())
			else:
				targets.add(Path(t).expanduser().resolve())

		for target in targets:
			patch_client_css(sourcedir, target, "Library")
			dev_reload(target)

		print(f"{TEXT_GREEN}{TEXT_CHECK} Done!{TEXT_RESET}")
