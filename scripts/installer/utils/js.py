#!/usr/bin/env python3

from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from enum import StrEnum
from typing import Self, Set, TYPE_CHECKING

from ..consts import *
from .log import *

ADW_JS_SOURCEMAP_COMMENT = b"//# sourceMappingURL="
ADW_JS_PATCH = b"document.head.append(Object.assign(document.createElement(\"script\"),{type:\"module\",src:\"/adwaita/js/shared.js\"}));"

if TYPE_CHECKING:
    from ..options.general import AdwInstallTarget

class AdwJSPatcher:
    def patch(self, target: AdwInstallTarget):
        script = target.steamui_dir / "library.js"
        script_bytes = script.read_bytes()

        comment_start = script_bytes.rfind(ADW_JS_SOURCEMAP_COMMENT)
        if comment_start == -1:
            if script_bytes.rfind(ADW_JS_PATCH) != -1:
                info(f"Script \"{script}\" is already patched")
                return
            else:
                raise ValueError(f"Failed to find injection point in \"{script}\"")

        comment_size = len(script_bytes) - comment_start
        patch_size = len(ADW_JS_PATCH)

        if patch_size > comment_size:
            critical(f"Patch size ({patch_size} bytes) exceeds the available space ({comment_size} bytes) in script: \"{script}\"")

        script.write_bytes(script_bytes[:comment_start] + ADW_JS_PATCH + b" " * max(0, comment_size - patch_size))
