#!/usr/bin/env python3

from __future__ import annotations

import json
from dataclasses import asdict
from typing import TYPE_CHECKING

from ..consts import *
from .args import *
from .log import *

ADW_JS_SOURCEMAP_COMMENT = b"//# sourceMappingURL="
ADW_JS_PATCH = b"document.head.append(Object.assign(document.createElement(\"script\"),{type:\"module\",src:\"/adwaita/js/shared.js\"}));"

if TYPE_CHECKING:
    from ..options.general import AdwInstallTarget

class AdwJSPatcher:
    def patch(self, target: AdwInstallTarget, options: dict[str, AdwParsedOptionGroup]):
        config_bytes = self._build_config(options).encode(encoding="utf-8")
        target.skin_config_js.write_bytes(config_bytes)

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

    def remove_patch(self, target: AdwInstallTarget):
        script = target.steamui_dir / "library.js"
        script_bytes = script.read_bytes()

        patch_start = script_bytes.rfind(ADW_JS_PATCH)
        if patch_start == -1: return

        patch_size = len(script_bytes) - patch_start
        comment_size = len(ADW_JS_SOURCEMAP_COMMENT)

        script.write_bytes(script_bytes[:patch_start] + ADW_JS_SOURCEMAP_COMMENT + b" " * max(0, patch_size - comment_size))

    def _build_config(self, options: dict[str, AdwParsedOptionGroup]) -> str:
        serialized = { key: asdict(group) for key, group in options.items() if key != "general" }
        config = json.dumps(serialized, indent=4, default=str)
        return f"export default {config};\n"
