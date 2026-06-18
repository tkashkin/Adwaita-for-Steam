#!/usr/bin/env python3

from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from enum import StrEnum
from typing import Self, Set, TYPE_CHECKING
import re

from ..consts import *
from .log import *

if TYPE_CHECKING:
    from ..options.general import AdwInstallTarget

ADW_PATCH_FILES = {
    "base": Path("library.css"),       # Login/Splash, some dialogs, also Big Picture
    "main": Path("gamerecording.css"), # Most of the main desktop windows
    "notes": Path("gamenotes.css")     # Notes
}

ADW_CSS_INDENT = " " * 4

ADW_CSS_RE_IMPORT = re.compile(r"^\s*@import\s+url\((?P<quote>[\"'])(?P<path>.+?)(?P=quote)\)\s*;\s*(?:/\*.*\*/\s*)?$")
ADW_CSS_RE_COMMENT = re.compile(r"/\*.*?\*/", re.S)
ADW_CSS_RE_BLOCK = re.compile(r"\s*([{};,])\s*")
ADW_CSS_RE_MULTISPACE = re.compile(r"\s+")

@dataclass
class AdwCSSImport:
    file: Path
    media_queries: list[str] | None = None
    comment: str | None = None

    def to_css(self) -> str:
        options = ""
        if self.media_queries:
            options += " " + " ".join([f"({q})" for q in self.media_queries])
        comment = f" /* {self.comment} */" if self.comment else ""
        return f"@import url(\"{self.file.as_posix()}\"){options};{comment}"

@dataclass
class AdwCSSBlock:
    selectors: list[str]
    rules: list[str]
    nested_blocks: list[Self] | None = None
    comment: str | None = None

    def to_css(self, indent: int = 0) -> str:
        if not self.selectors:
            raise ValueError("[AdwCSSBlock] CSS blocks must have at least one selector")

        css = ""
        indent_str = ADW_CSS_INDENT * indent

        if self.comment:
            css += f"{indent_str}/* {self.comment} */\n{indent_str}"

        css += f",\n{indent_str}".join(self.selectors) + f"\n{indent_str}{{"

        if self.rules:
            css += f"\n{indent_str}{ADW_CSS_INDENT}" + f"\n{indent_str}{ADW_CSS_INDENT}".join(self.rules) + "\n"

        if self.nested_blocks:
            css += f"\n" + "\n\n".join([b.to_css(indent + 1) for b in self.nested_blocks])

        return indent_str + css.strip() + f"\n{indent_str}}}"

@dataclass
class AdwCSSConfig:
    imports: list[AdwCSSImport]
    blocks: list[AdwCSSBlock]

class AdwCSSBuilder:
    _configs: list[AdwCSSConfig]

    def __init__(self, configs: list[AdwCSSConfig]):
        self._configs = configs

    def append(self, config: AdwCSSConfig):
        self._configs.append(config)

    def patch(self, target: AdwInstallTarget, optimize: bool):
        config_bytes = self._build_config().encode(encoding="utf-8")
        target.skin_config_css.write_bytes(config_bytes)
        
        for patch, file in ADW_PATCH_FILES.items():
            patch_bytes = self._build_patch(patch, optimize)

            if optimize:
                self._bundle_css(target.skin_dir / f"{patch}.css")

            original = target.css_dir / file.with_suffix(".original.css")
            patched = target.css_dir / file

            with patched.open(encoding="utf-8") as p:
                already_patched = p.readline(len(ADW_PATCH_HEADER)).strip() == ADW_PATCH_HEADER
            
            if not already_patched:
                patched.replace(original)
            
            original_size = original.stat().st_size
            patched_size = len(patch_bytes)
            if patched_size > original_size:
                critical(f"Patch size ({patched_size} bytes) exceeds the original file size ({original_size} bytes), original file: \"{original}\"")
            else:
                patch_bytes = patch_bytes + b" " * max(0, original_size - patched_size)
                patched.write_bytes(patch_bytes)

    def _build_config(self) -> str:
        imports = ""
        blocks = ""

        for c in self._configs:
            if c.imports:
                imports += "\n" + "\n".join([i.to_css() for i in c.imports])
            if c.blocks:
                blocks += "\n" + "\n\n".join([b.to_css() for b in c.blocks]) + "\n"

        return imports + "\n" + blocks
    
    def _build_patch(self, patch: str, optimize: bool) -> bytes:
        original = ADW_PATCH_FILES[patch].with_suffix(".original.css").name
        entrypoint = f"{patch}.min.css" if optimize else f"{patch}.css"
        content = [
            ADW_PATCH_HEADER,
            ADW_PATCH_VERSION_HEADER,
            ADW_PATCH_INSTALLATION_DATE_HEADER,
            f"@import url(\"{original}\");",
            f"@import url(\"../{ADW_ROOT}/{entrypoint}\");"
        ]
        if patch == "base":
            content.append(f"@import url(\"../{ADW_ROOT}/config.css\");")
        return ("\n".join(content) + "\n").encode(encoding="utf-8")
    
    def _bundle_css(self, file: Path) -> Path:
        bundle = file.with_suffix(".min.css")
        css = self._inline_css_imports(file)
        css = self._minify_css(css)
        bundle.write_text(css, encoding="utf-8")
        return bundle

    def _inline_css_imports(self, file: Path, seen: Set[Path] | None = None) -> str:
        seen = seen or set()
        file = file.resolve()
        if file in seen: return ""
        seen.add(file)

        result = []
        for line in file.read_text(encoding="utf-8").splitlines():
            match = ADW_CSS_RE_IMPORT.match(line)
            if match:
                result.append(self._inline_css_imports(file.parent / match.group("path"), seen))
            else:
                result.append(line)
        
        return "\n".join(result)
    
    def _minify_css(self, css: str) -> str:
        css = ADW_CSS_RE_COMMENT.sub("", css)
        css = ADW_CSS_RE_BLOCK.sub(r"\1", css)
        css = ADW_CSS_RE_MULTISPACE.sub(" ", css)
        return css.strip()