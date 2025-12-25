#!/usr/bin/env python3

from pathlib import Path
from dataclasses import dataclass
from enum import StrEnum
from typing import Self

from ..consts import *

ADW_CSS_INDENT = " " * 4

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

    def build(self) -> str:
        imports = ""
        blocks = ""

        for c in self._configs:
            if c.imports:
                imports += "\n" + "\n".join([i.to_css() for i in c.imports])
            if c.blocks:
                blocks += "\n" + "\n\n".join([b.to_css() for b in c.blocks]) + "\n"

        header = f"{ADW_PATCH_HEADER}\n{ADW_PATCH_VERSION_HEADER}\n{ADW_PATCH_INSTALLATION_DATE_HEADER}\n"
        return header + imports + "\n" + blocks

    def patch(self, target: Path, original: Path):
        content = self.build()
        original_size = original.stat().st_size
        with target.open("w", encoding="utf-8") as f:
            f.write(content)
            target_size = f.tell()
            if target_size < original_size:
                f.write(" " * (original_size - target_size))