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

TARGET_NORMAL = "~/.steam/steam"
TARGET_FLATPAK = "~/.var/app/com.valvesoftware.Steam/.steam/steam"

skindir = Path(SKIN_DIR)
patchdir = Path(PATCH_DIR)

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

	parser = ArgumentParser(description = "Adwaita-for-Steam installer")
	parser.add_argument("-t", "--target", nargs = "+", action = "extend", default = ["normal", "flatpak"], help = "Install targets: 'normal', 'flatpak', custom paths")
	parser.add_argument("-l", "--list-patches", action = "store_true", help = "List available patches and exit")
	parser.add_argument("-p", "--patch", nargs = "+", action = "extend", help = "Apply one or multiple patches")
	parser.add_argument("-n", "--name", default = SKIN_DIR, help = "Rename installed skin")
	args = parser.parse_args()

	if args.list_patches:
		list_patches(find_patches())
	
	with TemporaryDirectory() as tmpdir:
		sourcedir = skindir

		if args.patch:
			tmp = Path(tmpdir)
			sourcedir = tmp / SKIN_DIR
			print(f"Copying to the stage directory {TEXT_BOLD}{sourcedir}{TEXT_RESET}")
			shutil.copytree(skindir, sourcedir)
			for patch_file in args.patch:
				patch = patchdir / "{}{}".format(patch_file.removesuffix(".patch"), ".patch")
				if patch.exists():
					apply_patch(tmp, patch)
		
		targets = set()

		for t in args.target:
			match t:
				case "normal":
					targets.add(Path(TARGET_NORMAL).expanduser().resolve())
				case "flatpak":
					targets.add(Path(TARGET_FLATPAK).expanduser().resolve())
				case _:
					targets.add(Path(t).expanduser().resolve())

		for target in targets:
			install(sourcedir, target, args.name)