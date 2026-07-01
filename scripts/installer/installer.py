#!/usr/bin/env python3

from pprint import pp, pformat

from .consts import *

from .utils.args import *
from .utils.css import *
from .utils.fs import *
from .utils.log import *
from .utils.os_settings import *

from .options.general import *
from .options.style import *
from .options.colors import *
from .options.windowcontrols import *

class AdwInstaller:
    _logger: logging.Logger
    _options: dict[str, AdwParsedOptionGroup]
    _css: list[AdwCSSConfig]

    def __init__(self):
        self._check_dirs()
        self._parse_args()
        self._process()
    
    def _check_dir(self, dir: Path, name: str, required: bool = False):
        if not dir.is_dir():
            msg = f"{name} directory \"{dir}\" does not exist. Make sure you're running the installer from its root directory."
            if required:
                critical(msg)
            else:
                warning(msg)
    
    def _check_dirs(self):
        self._check_dir(dir=ADW_ROOT, name="Skin root", required=True)
        self._check_dir(dir=ADW_COLORTHEMES_DIR, name="Color themes")
        self._check_dir(dir=ADW_EXTRAS_DIR, name="Extras")
        self._check_dir(dir=ADW_FONTS_DIR, name="Fonts")
        self._check_dir(dir=ADW_WINDOWCONTROLS_DIR, name="Window controls")
    
    def _parse_args(self):
        args = AdwArgsParser(
            general=AdwGeneralOptions(),
            style=AdwStyleOptions(),
            colors=AdwColorOptions(),
            windowcontrols=AdwWindowControlsOptions()
        )
        (self._css, self._options) = args.parse()
        general: AdwGeneral = self._options["general"] # type: ignore

        if general.debug:
            logger.setLevel(logging.DEBUG)
            debug(f"Options:\n{pformat(self._options)}")

        if general.list_options:
            args.list_options()
            exit(0)
    
    def _process(self):
        general: AdwGeneral = self._options["general"] # type: ignore
        changes: int = 0
        if not general.targets:
            critical("No installation directories provided")
        for target in general.targets:
            target.update()
            match general.action:
                case AdwInstallAction.INSTALL:
                    if self._install(target, general.optimize):
                        changes += 1

                case AdwInstallAction.UNINSTALL:
                    if self._uninstall(target):
                        changes += 1
        if changes:
            match general.action:
                case AdwInstallAction.INSTALL:
                    success(f"Installed to {changes} {"directory" if changes == 1 else "directories"} successfully")
                
                case AdwInstallAction.UNINSTALL:
                    success(f"Uninstalled from {changes} {"directory" if changes == 1 else "directories"} successfully")
        else:
            info(f"No changes made")
    
    def _install(self, target: AdwInstallTarget, optimize: bool) -> bool:
        style: AdwStyle = self._options["style"] # type: ignore
        try:
            step(f"Installing to \"{target.root}\"")
            if not target.is_valid:
                warning(f"Directory \"{target.root}\" does not exist or is not a valid Steam directory, skipping")
                return False
            if target.is_v3_installed:
                warning("Previous version of the skin is installed, cleaning up")
                target.skin_v3_libraryroot_css.unlink(missing_ok=True)
                (target.css_dir / "library.original.css").replace(target.css_dir / "library.css")
            info("Copying skin directory")
            copy_dir(ADW_ROOT, target.skin_dir)
            if style.custom_css and style.custom_css.is_file():
                copy_file(style.custom_css, target.skin_custom_css)
            info("Patching and configuring skin")
            AdwCSSBuilder(self._css).patch(target, optimize)
            success(f"Installed to \"{target.root}\" successfully")
            return True
        except Exception as err:
            error(f"Failed to install to \"{target.root}\": {err}")
            return False
    
    def _uninstall(self, target: AdwInstallTarget) -> bool:
        try:
            step(f"Uninstalling from \"{target.root}\"")
            if not target.is_installed:
                warning(f"Not installed to \"{target.root}\", skipping")
                return False
            if target.is_v3_installed:
                warning("Previous version of the skin was installed, cleaning up")
                target.skin_v3_libraryroot_css.unlink(missing_ok=True)
            info("Restoring original styles")
            for file in ADW_PATCH_FILES.values():
                (target.css_dir / file.with_suffix(".original.css")).replace(target.css_dir / file)
            info("Removing skin directory")
            shutil.rmtree(target.skin_dir)
            success(f"Uninstalled from \"{target.root}\" successfully")
            return True
        except Exception as err:
            error(f"Failed to uninstall from \"{target.root}\": {err}")
            return False