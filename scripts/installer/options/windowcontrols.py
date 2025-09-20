#!/usr/bin/env python3

import sys
from argparse import _ArgumentGroup, Namespace
from enum import StrEnum
from collections.abc import Callable

from ..consts import *

from ..utils.args import *
from ..utils.css import *
from ..utils.log import *
from ..utils.os_settings import *

ADW_WINDOWCONTROLS_PRESETS = {
	"gnome": ":close",
	"pantheon": "close:maximize",
	"kde": ":minimize,maximize,close",
	"windows": ":minimize,maximize,close",
	"macos": "close,minimize,maximize:"
}

ADW_WINDOWCONTROLS_SELECTORS = {
	"minimize": ["&.minimizeButton"],
	"maximize": ["&.maximizeButton", "&.restoreButton"],
	"close": ["&.closeButton"]
}

ADW_WINDOWCONTROLS_SELECTORS_CHAT = {
    "left": ["html.client_chat_frame div.chat_main.singlewindow:not(:has(div.friendsListContainer.collapsed)) div.multiChatDialog &"],
    "right": ["html.client_chat_frame div.chat_main.singlewindow div.friendsListContainer:not(.collapsed) &"]
}

class AdwWindowControlsTheme(StrEnum):
    AUTO = "auto"
    ADWAITA = "adwaita"
    BREEZE = "breeze"
    WINDOWS = "windows"
    MACOS = "macos"

    @classmethod
    def resolve(cls, theme: str):
        match theme.lower():
            case cls.AUTO:
                match sys.platform:
                    case "linux":
                        match linux_get_current_desktop():
                            case "kde":
                                return cls.BREEZE
                            
                            case _:
                                return cls.ADWAITA
                    
                    case "win32" | "cygwin":
                        return cls.WINDOWS
                    
                    case "darwin":
                        return cls.MACOS
                    
                    case _:
                        return cls.ADWAITA

            case t:
                return cls(t)
    
    def __repr__(self) -> str:
        return self.value

@dataclass
class AdwWindowControlsLayout:
    preset: str
    layout: str

    def __init__(self, preset: str):
        self.preset = preset.lower()
        self.layout = AdwWindowControlsLayout._resolve_layout(self.preset)
    
    def to_css(self) -> AdwCSSBlock:
        (buttons_left, buttons_right) = [[b for b in s.split(",") if b in ADW_WINDOWCONTROLS_SELECTORS] for s in self.layout.split(":")]

        vars = [
            f"--adw-windowcontrols-left-has-buttons: { 0 if len(buttons_left) == 0 else 1 };",
            f"--adw-windowcontrols-left-buttons: { len(buttons_left) };",
            f"--adw-windowcontrols-right-has-buttons: { 0 if len(buttons_right) == 0 else 1 };",
            f"--adw-windowcontrols-right-buttons: { len(buttons_right) };",
            f"--adw-windowcontrols-close-margin: var(--adw-windowcontrols-buttons-margin-outer) + var(--adw-windowcontrols-button-width) + var(--adw-windowcontrols-buttons-margin-inner);",
            f"--adw-windowcontrols-close-margin-left: calc({ 1 if "close" in buttons_left else 0 } * (var(--adw-windowcontrols-close-margin)));",
            f"--adw-windowcontrols-close-margin-right: calc({ 1 if "close" in buttons_right else 0 } * (var(--adw-windowcontrols-close-margin)));"
        ]

        (buttons_left, buttons_right) = (list(enumerate(buttons_left)), list(enumerate(buttons_right)))
        buttons_left = map(AdwWindowControlsLayout._button_to_css("left"), buttons_left)
        buttons_right = map(AdwWindowControlsLayout._button_to_css("right"), buttons_right)

        return AdwCSSBlock(
            selectors=[":root"],
            rules=vars,
            nested_blocks=[
                AdwCSSBlock(
                    selectors=["body.DesktopUI", "html.client_chat_frame"],
                    rules=[],
                    nested_blocks=[
                        AdwCSSBlock(
                            selectors=[".title-bar-actions .title-area-icon"],
                            rules=["visibility: hidden !important;"],
                            nested_blocks=[*buttons_left, *buttons_right]
                        )
                    ]
                )
            ],
            comment=f"Window controls layout: {self.preset} - {self.layout}"
        )
    
    @staticmethod
    def _resolve_layout(preset: str) -> str:
        if preset == "auto":
            match sys.platform:
                case "linux":
                    match linux_get_current_desktop():
                        case "gnome":
                            return linux_get_setting("org.gnome.desktop.wm.preferences", "button-layout") or ADW_WINDOWCONTROLS_PRESETS["gnome"]
                        
                        case desktop:
                            return ADW_WINDOWCONTROLS_PRESETS.get(desktop) or ADW_WINDOWCONTROLS_PRESETS["gnome"]
                
                case "win32" | "cygwin":
                    return ADW_WINDOWCONTROLS_PRESETS["windows"]
                
                case "darwin":
                    return ADW_WINDOWCONTROLS_PRESETS["macos"]
                
        elif preset in ADW_WINDOWCONTROLS_PRESETS:
            return ADW_WINDOWCONTROLS_PRESETS[preset]
        
        if not preset: preset = ":"
        if ":" not in preset: preset = ":" + preset
        
        return preset
    
    @staticmethod
    def _button_to_css(side: str) -> Callable[[tuple[int, str]], AdwCSSBlock]:
        return lambda b: AdwCSSBlock(
            selectors=ADW_WINDOWCONTROLS_SELECTORS[b[1]],
            rules=[
                "visibility: visible !important;",
                f"{side}: calc(var(--adw-windowcontrols-buttons-margin-outer) + {b[0]} * (var(--adw-windowcontrols-button-width)) + {b[0]} * (var(--adw-windowcontrols-button-gap))) !important;"
            ],
            nested_blocks=[
                AdwCSSBlock(
                    selectors=ADW_WINDOWCONTROLS_SELECTORS_CHAT[side],
                    rules=["visibility: hidden !important;"]
                )
            ]
        )
        

@dataclass
class AdwWindowControls(AdwParsedOptionGroup):
    theme: AdwWindowControlsTheme
    layout: AdwWindowControlsLayout

    def to_css(self) -> AdwCSSConfig:
        return AdwCSSConfig(
            imports=[
                AdwCSSImport(
                    file=Path("..") / ADW_ROOT / ADW_WINDOWCONTROLS / f"{self.theme}.css",
                    comment=f"Window controls theme: {self.theme}"
                )
            ],
            blocks=[self.layout.to_css()]
        )

class AdwWindowControlsOptions(AdwOptionGroup):
    title = "window controls"

    def add_options(self, args: _ArgumentGroup):
        args.add_argument(
            "-wt",
            "--windowcontrols-theme",
            help="set window controls theme\n'auto' will be replaced by your system theme if possible",
            default="auto",
            choices=AdwWindowControlsTheme,
            type=AdwWindowControlsTheme.resolve
        )
        args.add_argument(
            "-wl",
            "--windowcontrols-layout",
            help="set window controls layout\n'auto' will be replaced by your system layout if possible\nCUSTOM_LAYOUT can be an arbitrary GNOME button layout string",
            metavar="{auto," + ",".join(ADW_WINDOWCONTROLS_PRESETS.keys()) + ",CUSTOM_LAYOUT}",
            default="auto",
            type=AdwWindowControlsLayout
        )
    
    def parse(self, args: Namespace) -> AdwWindowControls:
        return AdwWindowControls(
            theme=args.windowcontrols_theme,
            layout=args.windowcontrols_layout
        )