#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import NoReturn
import configparser
import re
import subprocess
import shutil
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

COLOR_THEME_DIR = "extras/colorthemes"
PATCH_DIR = "extras/patches"
SKIN_DIR = "Adwaita"
WEB_EXTRAS_DIR = "extras/web/extras"
WEB_THEME_DIR = "extras/web"

ASSETS_DIR = "assets"
COLORS_FILE = "adw/colors.styles"
CSS_FILE = "resource/webkit.css"

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"

skindir = Path(SKIN_DIR)
patchdir = Path(PATCH_DIR)
webthemedir = Path(WEB_THEME_DIR)
webextrasdir = Path(WEB_EXTRAS_DIR)
colorthemedir = Path(COLOR_THEME_DIR)

WEB_BASE_FILES = [
	webthemedir / "base/1_root.css",
	webthemedir / "base/3_library.css",
	webthemedir / "base/4_collections.css",
	webthemedir / "base/5_game_details.css",
	webthemedir / "base/6_downloads.css",
	webthemedir / "base/7_dialogs.css",
	webthemedir / "base/9_scrollbars.css",
	webthemedir / "base/10_login.css",
	webthemedir / "base/11_launch_options.css",
]

WEB_FULL_FILES = [
	webthemedir / "base/1_root.css",
	webthemedir / "full/2_global.css",
	webthemedir / "base/3_library.css",
	webthemedir / "full/3_library.css",
	webthemedir / "base/4_collections.css",
	webthemedir / "base/5_game_details.css",
	webthemedir / "full/5_game_details.css",
	webthemedir / "base/6_downloads.css",
	webthemedir / "full/6_downloads.css",
	webthemedir / "base/7_dialogs.css",
	webthemedir / "full/7_dialogs.css",
	webthemedir / "full/8_chat.css",
	webthemedir / "base/9_scrollbars.css",
	webthemedir / "base/10_login.css",
	webthemedir / "base/11_launch_options.css",
	webthemedir / "full/12_content_management.css",
]

SHARED_PATCHES = [
	"windowcontrols/hide-close",
	"windowcontrols/right-all",
	"windowcontrols/left-all",
	"windowcontrols/left",
]

# List Options
def list_options(type: str, options: list[Path], suffix: str, sourcedir: Path, arg: str) -> NoReturn:
	if options:
		print(f"{TEXT_BLUE}{TEXT_BOLD}{type.upper()}: {len(options)}{TEXT_RESET}")
		for option in options:
			name = os.path.relpath(option, sourcedir).removesuffix(suffix)

			if type == "color themes":
				name = name.split("/")[1]

			description = ""

			if type == "patches":
				with option.open() as patch_file:
					description = " - {}".format(patch_file.readline().removeprefix("#").strip())

			print(f"{TEXT_PURPLE}{TEXT_BOLD}{name}{TEXT_RESET}{description}")
		print(f"\nApply {type} using {TEXT_GREEN}'./install.py --{arg} NAME'{TEXT_RESET}\n")
	else:
		print(f"{TEXT_PURPLE}{TEXT_INFO} No {type} available\n{TEXT_RESET}")

# Patches
def find_patches() -> list[Path]:
	return list(patchdir.glob("**/*.patch"))

def patch_name(patch: Path) -> str:
	return os.path.relpath(patch, patchdir).removesuffix(".patch")

def apply_patch(parentdir: Path, patch: Path):
	with patch.open() as patch_file:
		print(f"\n{TEXT_BLUE}{TEXT_ARROW} Applying patch {TEXT_BOLD}{patch_name(patch)}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
		try:
			subprocess.run(["patch", "-l", "-p0"], cwd = parentdir, stdin = patch_file)
		except Exception as e:
			print(f"\n{TEXT_RED}{TEXT_CROSS} Error applying patch: {e}{TEXT_RESET}")

# Webkit CSS
def find_web_extras() -> list[Path]:
	return list(webextrasdir.glob("**/*.css"))

def gen_webkit_theme(target: Path, name: str, selected_extras: list[Path]):
	if name == "none":
		return
	elif name == "base":
		selected_files = WEB_BASE_FILES
	elif name == "full":
		selected_files = WEB_FULL_FILES
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
					f = webthemedir / "extras/{}{}".format(we, ".css")

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

def hex2rgba(hex: str) -> tuple:
	return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5, 7))

def rgba2vgui(name: str, rgba: tuple) -> str:
	return f'{name}="{rgba[0]} {rgba[1]} {rgba[2]} {rgba[3]}"'

def hex2css(name: str, hex: str) -> str:
	return f'--{name}: {hex};'

def hex2vgui(name: str, hex: str) -> str:
	return rgba2vgui(name, hex2rgba(hex))

def replace_css_colors(target: Path, config: configparser.ConfigParser):
	with open (target, 'r' ) as f:
		content = f.read()

	for section in config.sections():
		for (key, val) in config.items(section):
			s = hex2css(key, val)
			content = re.sub(f'^(\s+)--{key}: [^;]+;$', r'\1' + s, content, flags = re.M)

	with open (target, 'w' ) as f:
		f.write(content)

def replace_vgui_colors(target: Path, config: configparser.ConfigParser):
	with open (target, 'r' ) as f:
		content = f.read()

	for section in config.sections():
		if section == "font":
			continue

		for (key, val) in config.items(section):
			s = hex2vgui(key, val)
			content = re.sub(f'^(\s+){key}="[^"]+"$', r'\1' + s, content, flags = re.M)

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

if __name__ == "__main__":
	if not skindir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Skin directory {TEXT_BOLD}{SKIN_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")
	if not webthemedir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Web Theme directory {TEXT_BOLD}{WEB_THEME_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")
	if not colorthemedir.exists():
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} Color Theme directory {TEXT_BOLD}{COLOR_THEME_DIR}{TEXT_RESET}{TEXT_RED} does not exist. Make sure you're running the installer from its root directory{TEXT_RESET}")

	parser = ArgumentParser(description = "Adwaita-for-Steam installer")
	parser.add_argument("-c", "--color-theme", default = "adwaita", help = "Choose color theme")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", default = ["normal", "flatpak"], help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-l", "--list-options", action = "store_true", help = "List available patches, themes, web extras and exit")
	parser.add_argument("-p", "--patch", nargs = "+", action = "extend", help = "Apply one or multiple patches")
	parser.add_argument("-n", "--name", default = SKIN_DIR, help = "Rename installed skin")
	parser.add_argument("-w", "--web-theme", choices = ["base", "full", "none"], default = "base", help = "Choose web theme variant")
	parser.add_argument("-we", "--web-extras", nargs = "+", action = "extend", help = "Enable one or multiple web theme extras")
	args = parser.parse_args()

	if args.list_options:
		list_options("patches", find_patches(), ".patch", patchdir, "patch")
		list_options("color themes", find_color_themes(), ".theme", colorthemedir, "color-theme")
		list_options("web extras", find_web_extras(), ".css", webextrasdir, "web-extras")
		exit(0)

	if args.patch and not shutil.which("patch"):
		raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} {TEXT_BOLD}patch{TEXT_RESET}{TEXT_RED} executable not found in $PATH. Make sure you have GNU Patch installed{TEXT_RESET}")

	if args.color_theme:
		ct = Path(args.color_theme)
		cta = ct.parents[0] / "assets"

		if args.color_theme.removesuffix(".theme") == "adwaita":
			selected_theme = None
		elif ct.exists() and ct.suffix == ".theme" and cta.exists():
			selected_theme = ct
			selected_theme_assets = cta
		else:
			t = args.color_theme.removesuffix(".theme")
			selected_theme = colorthemedir / "{}/{}{}".format(t, t, ".theme")
			selected_theme_assets = colorthemedir / "{}/{}".format(t, "assets")
			if not selected_theme.exists():
				raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_RED} theme not found.{TEXT_RESET}")
			if not selected_theme_assets.exists():
				raise SystemExit(f"{TEXT_RED}{TEXT_CROSS} {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_RED} theme assets not found.{TEXT_RESET}")

	with TemporaryDirectory() as tmpdir:
		tmp = Path(tmpdir)
		sourcedir = tmp / SKIN_DIR
		print(f"{TEXT_BLUE}{TEXT_ARROW} Copying to the stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")
		shutil.copytree(skindir, sourcedir)

		if args.patch:
			for patch_file in args.patch:

				pf = Path(patch_file)
				if pf.exists() and pf.suffix == ".patch":
					patch = pf
					p = None
				else:
					p = patch_file.removesuffix(".patch")
					patch = patchdir / "{}{}".format(p, ".patch")

				if patch.exists():
					if [s for s in SHARED_PATCHES if p == s]:
						if not args.web_extras:
							args.web_extras = [p]
						elif not [s for s in args.web_extras if p in s]:
							args.web_extras.append(p)
					apply_patch(tmp, patch)
				else:
					print(f"{TEXT_PURPLE}{TEXT_INFO} {patch} not found.{TEXT_RESET}")

		gen_webkit_theme(sourcedir / CSS_FILE, args.web_theme, args.web_extras)

		if selected_theme:
			print(f"{TEXT_BLUE}{TEXT_ARROW} Applying color theme {TEXT_BOLD}{selected_theme}{TEXT_RESET}{TEXT_BLUE}...{TEXT_RESET}")
			config = configparser.ConfigParser()
			config.read(selected_theme)
			replace_css_colors(sourcedir / CSS_FILE, config)
			replace_vgui_colors(sourcedir / COLORS_FILE, config)
			shutil.copytree(selected_theme_assets, sourcedir / ASSETS_DIR, dirs_exist_ok=True)

		targets = set()

		for t in args.target:
			if t == "normal":
				targets.add(Path(TARGET_NORMAL).expanduser().resolve())
			elif t == "flatpak":
				targets.add(Path(TARGET_FLATPAK).expanduser().resolve())
			else:
				targets.add(Path(t).expanduser().resolve())

		for target in targets:
			install(sourcedir, target, args.name)
		print(f"{TEXT_GREEN}{TEXT_CHECK} Done!{TEXT_RESET}")
