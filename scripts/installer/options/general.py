#!/usr/bin/env python3

from argparse import _ArgumentGroup, Namespace
from dataclasses import dataclass, field
from enum import StrEnum

from ..consts import *

from ..utils.args import *
from ..utils.css import *
from ..utils.log import *
from ..utils.os_settings import *

match sys.platform:
    case "linux":
        ADW_INSTALL_TARGETS: dict[str, Path] = {
            "default": Path("~/.steam/steam"),
            "flatpak": Path("~/.var/app/com.valvesoftware.Steam/.steam/steam"),
            "snap": Path("~/snap/steam/common/.steam/steam")
        }

    case "win32" | "cygwin":
        ADW_INSTALL_TARGETS: dict[str, Path] = {
            "default": Path("C:\\Program Files (x86)\\Steam")
        }

    case "darwin":
        ADW_INSTALL_TARGETS: dict[str, Path] = {
            "default": Path("~/Library/Application Support/Steam/Steam.AppBundle/Steam/Contents/MacOS")
        }

class AdwInstallAction(StrEnum):
    INSTALL = "install"
    UNINSTALL = "uninstall"

    def __repr__(self) -> str:
        return self.value

@dataclass
class AdwInstallTarget:
    root: Path
    is_valid: bool
    is_installed: bool
    is_old_version_installed: bool

    steamui_dir: Path = field(repr=False)
    css_dir: Path = field(repr=False)
    patch_css: Path = field(repr=False)
    patch_css_original: Path = field(repr=False)
    skin_dir: Path = field(repr=False)
    skin_config_css: Path = field(repr=False)
    skin_custom_css: Path = field(repr=False)
    skin_old_libraryroot_css: Path = field(repr=False)

    def __init__(self, root: Path):
        self.root = root.expanduser().resolve()
        self.steamui_dir = self.root / "steamui"
        self.css_dir = self.steamui_dir / "css"
        self.patch_css = self.css_dir / "library.css"
        self.patch_css_original = self.css_dir / "library.original.css"
        self.skin_dir = self.steamui_dir / ADW_ROOT
        self.skin_custom_css = self.skin_dir / "custom.css"
        self.skin_old_libraryroot_css = self.steamui_dir / "libraryroot.custom.css"
        self.update()

    def update(self):
        self.is_valid = self.css_dir.is_dir() and self.patch_css.is_file()
        if self.is_valid and self.patch_css_original.is_file():
            with self.patch_css.open(encoding="utf-8") as patch_css:
                header = patch_css.readline(max(len(ADW_PATCH_HEADER), len(ADW_PATCH_OLD_HEADER))).strip()
                self.is_installed = header in [ADW_PATCH_HEADER, ADW_PATCH_OLD_HEADER]
                self.is_old_version_installed = header == ADW_PATCH_OLD_HEADER or self.skin_old_libraryroot_css.is_file()
        else:
            self.is_installed = False
            self.is_old_version_installed = False

@dataclass
class AdwGeneral(AdwParsedOptionGroup):
    action: AdwInstallAction
    targets: list[AdwInstallTarget]
    debug: bool

    def to_css(self) -> None:
        return None

class AdwGeneralOptions(AdwOptionGroup):
    def add_options(self, args: _ArgumentGroup):
        args.add_argument(
            "-t",
            "--target",
            help="install to one or more Steam installation paths",
            metavar="{" + ",".join(ADW_INSTALL_TARGETS.keys()) + ",CUSTOM_PATH}",
            nargs="+",
            action="extend"
        )
        args.add_argument(
            "-u",
            "--uninstall",
            help="uninstall from one or more Steam installation paths",
            action="store_true"
        )
        args.add_argument(
            "-d",
            "--debug",
            help="show more debug output",
            action="store_true"
        )
        args.add_argument(
            "-h",
            "--help",
            help="show this help message and exit",
            action="help"
        )
        args.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"Adwaita-for-Steam {ADW_VERSION}"
        )

    def parse(self, args: Namespace) -> AdwGeneral:
        return AdwGeneral(
            action=AdwInstallAction.UNINSTALL if args.uninstall else AdwInstallAction.INSTALL,
            targets=self._resolve_targets(args.target),
            debug=args.debug
        )

    def _resolve_targets(self, targets: list[str] | None) -> list[AdwInstallTarget]:
        resolved_targets: list[AdwInstallTarget] = []

        if not targets:
            targets = list(ADW_INSTALL_TARGETS.keys())

        for t in targets:
            target = self._resolve_target(t)
            if target:
                resolved_targets.append(target)

        return resolved_targets

    def _resolve_target(self, target: str) -> AdwInstallTarget | None:
        match target:
            case "default":
                return AdwInstallTarget(self._get_default_target_path())

            case t if t in ADW_INSTALL_TARGETS:
                return AdwInstallTarget(ADW_INSTALL_TARGETS[t])

            case t:
                path = Path(t)
                return AdwInstallTarget(path) if path.is_dir() else None

    def _get_default_target_path(self) -> Path:
        path = ADW_INSTALL_TARGETS["default"]
        match sys.platform:
            case "win32" | "cygwin":
                try:
                    import winreg
                    reg_path = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\Valve\\Steam"), "InstallPath")[0]
                    path = Path(reg_path)
                except: pass
        return path