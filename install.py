#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import NoReturn
import subprocess
import shutil
import os

TEXT_BOLD = "\033[1m"
TEXT_RESET = "\033[0m"

SKIN_DIR = "Adwaita"
PATCH_DIR = "patches"
WEB_THEME_DIR = "web_themes"

CSS_FILE = "resource/webkit.css"

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"

skindir = Path(SKIN_DIR)
patchdir = Path(PATCH_DIR)
webthemedir = Path(WEB_THEME_DIR)

WEB_BASE_FILES = [
	webthemedir / "base/1_root.css",
	webthemedir / "base/3_library.css",
	webthemedir / "base/4_collections.css",
	webthemedir / "base/5_game_details.css",
	webthemedir / "base/6_downloads.css",
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
]

def find_patches() -> list[Path]:
	return list(patchdir.glob("**/*.patch"))

def patch_name(patch: Path) -> str:
	return os.path.relpath(patch, patchdir).removesuffix(".patch")

def list_patches(patches: list[Path]) -> NoReturn:
	if patches:
		print(f"{len(patches)} patches available:\n")
		for patch in patches:
			patch_name = os.path.relpath(patch, patchdir).removesuffix(".patch")
			patch_description = ""
			with patch.open() as patch_file:
				patch_description = " - {}".format(patch_file.readline().removeprefix("#").strip())
			print(f"{TEXT_BOLD}{patch_name}{TEXT_RESET}{patch_description}")
		print(f"\nApply patches using {TEXT_BOLD}'./install.py --patch PATCH_NAME'{TEXT_RESET}")
	else:
		print("No patches available")
	exit(0)

def apply_patch(parentdir: Path, patch: Path):
	with patch.open() as patch_file:
		print(f"\nApplying patch {TEXT_BOLD}{patch_name(patch)}{TEXT_RESET}...")
		try:
			subprocess.run(["patch", "-l", "-p0"], cwd = parentdir, stdin = patch_file)
		except Exception as e:
			print(f"\nError applying patch: {e}")

def gen_webkit_theme(target: Path, name: str, selected_extras: list[Path]):
	if name == "none":
		return
	elif name == "base":
		selected_files = WEB_BASE_FILES
	elif name == "full":
		selected_files = WEB_FULL_FILES
	else:
		raise SystemExit(f"Invalid web theme selected: {name}")

	with open(target,'wb') as wfd:
		for f in selected_files:
			with open(f,'rb') as fd:
				shutil.copyfileobj(fd, wfd)

		if selected_extras:
			print()
			for f in selected_extras:
				we = f.removesuffix(".css")
				f = webthemedir / "extras/{}{}".format(we, ".css")
				if f.exists():
					with open(f,'rb') as fd:
						print(f"Applying web_extra {TEXT_BOLD}{we}{TEXT_RESET}...")
						shutil.copyfileobj(fd, wfd)
				else:
					print(f"Web Extra: {TEXT_BOLD}{f}{TEXT_RESET} not found!")
			print()

def install(source: Path, target: Path, name: str):
	if target.is_dir():
		if target.stem != "skins":
			target = target / "skins"
			target.mkdir(exist_ok = True)
	else:
		print(f"Directory {TEXT_BOLD}{target}{TEXT_RESET} does not exist")
		return
	print(f"Installing skin {TEXT_BOLD}{name}{TEXT_RESET} into {TEXT_BOLD}{target}{TEXT_RESET}...")
	target_skin = target / name
	if target_skin.exists():
		shutil.rmtree(target_skin)
	shutil.copytree(source, target_skin)

if __name__ == "__main__":
	if not skindir.exists():
		raise SystemExit(f"Skin directory {TEXT_BOLD}{SKIN_DIR}{TEXT_RESET} does not exist. Make sure you're running the installer from its root directory")
	if not webthemedir.exists():
		raise SystemExit(f"Web Theme directory {TEXT_BOLD}{WEB_THEME_DIR}{TEXT_RESET} does not exist. Make sure you're running the installer from its root directory")

	parser = ArgumentParser(description = "Adwaita-for-Steam installer")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", default = ["normal", "flatpak"], help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-l", "--list-patches", action = "store_true", help = "List available patches and exit")
	parser.add_argument("-p", "--patch", nargs = "+", action = "extend", help = "Apply one or multiple patches")
	parser.add_argument("-n", "--name", default = SKIN_DIR, help = "Rename installed skin")
	parser.add_argument("-w", "--web-theme", choices = ["base", "full", "none"], default = "base", help = "Choose web theme variant")
	parser.add_argument("-we", "--web-extras", nargs = "+", action = "extend", help = "Enable one or multiple web theme extras")
	args = parser.parse_args()

	if args.list_patches:
		list_patches(find_patches())

	if args.patch and not shutil.which("patch"):
		raise SystemExit(f"{TEXT_BOLD}patch{TEXT_RESET} executable not found in $PATH. Make sure you have GNU Patch installed")

	with TemporaryDirectory() as tmpdir:
		tmp = Path(tmpdir)
		sourcedir = tmp / SKIN_DIR
		print(f"Copying to the stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")
		shutil.copytree(skindir, sourcedir)

		if args.patch:
			for patch_file in args.patch:
				p = patch_file.removesuffix(".patch")
				patch = patchdir / "{}{}".format(p, ".patch")

				if patch.exists():
					if [s for s in SHARED_PATCHES if p == s]:
						if not args.web_extras:
							args.web_extras = [p]
						elif not [s for s in args.web_extras if p in s]:
							args.web_extras.append(p)

					apply_patch(tmp, patch)

		gen_webkit_theme(sourcedir / CSS_FILE, args.web_theme, args.web_extras)

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
