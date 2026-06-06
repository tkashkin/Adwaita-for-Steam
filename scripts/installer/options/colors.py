#!/usr/bin/env python3

import sys
from argparse import _ArgumentGroup, Namespace
from dataclasses import dataclass
from enum import StrEnum

from ..consts import *

from ..utils.args import *
from ..utils.css import *
from ..utils.log import *
from ..utils.os_settings import *

ADW_NAMED_ACCENT_COLORS: list[str] = ["blue", "teal", "green", "yellow", "orange", "red", "pink", "purple", "slate"]
ADW_WINDOWS_DEFAULT_ACCENT_COLOR: str = "#0078d4"
ADW_MACOS_ACCENT_COLORS: dict[int | None, str] = {
    None: "#007aff",
    -1: "#8c8c8c",
    0: "#ff5257",
    1: "#f7821b",
    2: "#ffc600",
    3: "#62ba46",
    4: "#007aff",
    5: "#a550a7",
    6: "#f74f9e"
}

class AdwColorScheme(StrEnum):
    AUTO = "auto"
    DARK = "dark"
    LIGHT = "light"

    def __repr__(self) -> str:
        return self.value

@dataclass
class AdwAccentColor:
    color: str
    css_color: str

    def __init__(self, color: str):
        self.color = color
        self.css_color = AdwAccentColor._color_to_css(self.color)

    def to_css(self) -> str:
        return f"--adw-system-accent: {self.css_color};"

    @staticmethod
    def _color_to_css(color: str) -> str:
        match color.lower():
            case c if c in ADW_NAMED_ACCENT_COLORS:
                return f"var(--adw-accent-{c})"
            case "auto":
                return AdwAccentColor._color_to_css(AdwAccentColor._get_system_accent_color())
            case c if c.startswith("#") and len(c) in [4, 7]:
                return c
            case c if c.startswith("rgb(") and c.endswith(")"):
                return c
            case c:
                raise ValueError(f"[AdwAccentColor._color_to_css] Invalid color: {c}")

    @staticmethod
    def _get_system_accent_color() -> str:
        try:
            match sys.platform:
                case "linux":
                    if linux_get_current_desktop() == "gnome":
                        gnome_accent_color = linux_get_setting("org.gnome.desktop.interface", "accent-color")
                        if gnome_accent_color: return str(gnome_accent_color)
                    fdo_accent_color = linux_get_setting("org.freedesktop.appearance", "accent-color")
                    if fdo_accent_color and len(fdo_accent_color) == 3:
                        return "#" + "".join(format(round(float(c) * 255), "02x") for c in fdo_accent_color)
                    return ADW_NAMED_ACCENT_COLORS[0]

                case "win32" | "cygwin":
                    import winreg
                    accent_palette = win32_get_reg_value(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent", "AccentPalette")
                    if not accent_palette:
                        return ADW_WINDOWS_DEFAULT_ACCENT_COLOR
                    accent_palette = [f"{byte:02x}" for byte in accent_palette]
                    if len(accent_palette) < 15:
                        return ADW_WINDOWS_DEFAULT_ACCENT_COLOR
                    return "#" + accent_palette[12] + accent_palette[13] + accent_palette[14]

                case "darwin":
                    accent_color = darwin_get_setting("AppleAccentColor")
                    return ADW_MACOS_ACCENT_COLORS[int(accent_color) if accent_color else None]

                case p:
                    raise ValueError(f"[AdwAccentColor._get_system_accent_color] Unsupported platform: {p}")
        except:
            return ADW_NAMED_ACCENT_COLORS[0]

@dataclass
class AdwColors(AdwParsedOptionGroup):
    color_theme: str
    accent_color: AdwAccentColor
    color_scheme: AdwColorScheme

    def to_css(self) -> AdwCSSConfig:
        imports = []
        vars = []
        blocks = []

        if self.color_theme != "adwaita":
            imports.append(
                AdwCSSImport(
                    file=ADW_COLORTHEMES / self.color_theme / f"{self.color_theme}.css",
                    comment=f"Color theme: {self.color_theme}"
                )
            )

        if self.accent_color:
            vars.append(self.accent_color.to_css())

        if self.color_scheme != AdwColorScheme.AUTO:
            vars.append(f"--adw-color-scheme: {self.color_scheme};")

        if vars:
            blocks.append(
                AdwCSSBlock(
                    selectors=[":root"],
                    rules=vars,
                    comment=f"Accent color: {self.accent_color.color}, color scheme: {self.color_scheme}"
                )
            )

        return AdwCSSConfig(
            imports=imports,
            blocks=blocks
        )

class AdwColorOptions(AdwOptionGroup):
    title = "colors"

    _color_themes: list[str]

    def __init__(self):
        self._color_themes = AdwColorOptions._find_color_themes()

    def add_options(self, args: _ArgumentGroup):
        args.add_argument(
            "-c",
            "--color-theme",
            help="use one of the available color themes",
            metavar="THEME",
            default="adwaita",
            choices=self._color_themes,
            type=str.lower
        )
        args.add_argument(
            "-a",
            "--accent-color",
            help="set accent color\n'auto' will use your system accent color if possible\ncustom colors must be formatted as '#RGB', '#RRGGBB', or 'rgb(r, g, b)'",
            metavar="{auto," + ",".join(ADW_NAMED_ACCENT_COLORS) + ",ACCENT_COLOR}",
            default="auto",
            type=AdwAccentColor
        )
        args.add_argument(
            "-s",
            "--color-scheme",
            help="set color scheme\n'auto' will use your system settings for dark or light appearance if supported",
            default="auto",
            choices=AdwColorScheme,
            type=AdwColorScheme
        )

    def parse(self, args: Namespace) -> AdwColors:
        return AdwColors(
            color_theme=args.color_theme,
            accent_color=args.accent_color,
            color_scheme=args.color_scheme
        )

    def list_options(self):
        print("\nAvailable color themes:\n\n* " + "\n* ".join(self._color_themes))
        print("\nApply a color theme using ./install.py --color-theme THEME")

    @staticmethod
    def _find_color_themes() -> list[str]:
        return sorted([t.parts[2] for t in ADW_COLORTHEMES_DIR.glob("*/*.css")])