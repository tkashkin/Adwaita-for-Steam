#!/usr/bin/env python3

from argparse import _ArgumentGroup, Namespace
from dataclasses import dataclass

from ..consts import *

from ..utils.args import *
from ..utils.css import *
from ..utils.log import *
from ..utils.os_settings import *

@dataclass
class AdwStyle(AdwParsedOptionGroup):
    extras: list[str]
    font: str
    custom_css: bool

    def to_css(self) -> AdwCSSConfig:
        imports = [
            AdwCSSImport(
                file=Path("library.original.css"),
                comment="Base Steam styles"
            ),
            AdwCSSImport(
                file=Path("..") / ADW_ROOT / "adwaita.css",
                comment="Main theme styles"
            )
        ]

        for extra in self.extras:
            imports.append(
                AdwCSSImport(
                    file=Path("..") / ADW_ROOT / ADW_EXTRAS / f"{extra}.css",
                    comment=f"Extra: {extra}"
                )
            )

        imports.append(
            AdwCSSImport(
                file=Path("..") / ADW_ROOT / ADW_FONTS / self.font / f"{self.font}.css",
                comment=f"Font: {self.font}"
            )
        )

        if self.custom_css:
            imports.append(
                AdwCSSImport(
                    file=Path("..") / ADW_ROOT / "custom.css",
                    comment="Custom CSS"
                )
            )

        return AdwCSSConfig(
            imports=imports,
            blocks=[]
        )

class AdwStyleOptions(AdwOptionGroup):
    title = "style"

    _extras: list[str]
    _fonts: list[str]

    def __init__(self):
        self._extras = AdwStyleOptions._find_extras()
        self._fonts = AdwStyleOptions._find_fonts()

    def add_options(self, args: _ArgumentGroup):
        args.add_argument(
            "-e",
            "--extra",
            "--extras",
            dest="extras",
            help="enable one or multiple theme extras",
            metavar="EXTRA",
            nargs="+",
            action="extend",
            default=[],
            choices=self._extras
        )
        args.add_argument(
            "-f",
            "--font",
            help="set font family",
            default="adwaita",
            choices=self._fonts
        )
        args.add_argument(
            "--custom-css",
            help="enable custom CSS",
            action="store_true"
        )

    def parse(self, args: Namespace) -> AdwStyle:
        return AdwStyle(
            extras=args.extras,
            font=args.font,
            custom_css=args.custom_css
        )

    def list_options(self):
        print("Available extras:\n\n* " + "\n* ".join(self._extras))
        print("\nApply extras using ./install.py --extras EXTRA1 EXTRA2...")

    @staticmethod
    def _find_extras() -> list[str]:
        return sorted(["/".join(e.parts[2:]).removesuffix(".css") for e in ADW_EXTRAS_DIR.glob("*/*.css")])

    @staticmethod
    def _find_fonts() -> list[str]:
        return sorted([t.parts[2] for t in ADW_FONTS_DIR.glob("*/*.css")])