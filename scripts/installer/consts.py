#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime

ADW_ROOT = Path("adwaita")
ADW_CUSTOM = Path("custom")

ADW_COLORTHEMES = Path("colorthemes")
ADW_EXTRAS = Path("extras")
ADW_FONTS = Path("fonts")
ADW_WINDOWCONTROLS = Path("windowcontrols")

ADW_COLORTHEMES_DIR = ADW_ROOT / ADW_COLORTHEMES
ADW_EXTRAS_DIR = ADW_ROOT / ADW_EXTRAS
ADW_FONTS_DIR = ADW_ROOT / ADW_FONTS
ADW_WINDOWCONTROLS_DIR = ADW_ROOT / ADW_WINDOWCONTROLS

ADW_VERSION = (ADW_ROOT / "VERSION").read_text()

ADW_PATCH_HEADER_V3 = "/*patched*/"
ADW_PATCH_HEADER = "/* Adwaita-for-Steam */"
ADW_PATCH_VERSION_HEADER = f"/* Version: {ADW_VERSION} */"
ADW_PATCH_INSTALLATION_DATE_HEADER = f"/* Installed at: {datetime.now():%Y-%m-%d %H:%M:%S} */"