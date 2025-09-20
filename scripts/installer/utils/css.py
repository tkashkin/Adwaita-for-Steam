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
        return f"@import url(\"{self.file}\"){options};{comment}"

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
            css += f"{indent_str}/* {self.comment} */\r\n{indent_str}"

        css += f",\r\n{indent_str}".join(self.selectors) + f"\r\n{indent_str}{{"

        if self.rules:
            css += f"\r\n{indent_str}{ADW_CSS_INDENT}" + f"\r\n{indent_str}{ADW_CSS_INDENT}".join(self.rules) + "\r\n"

        if self.nested_blocks:
            css += f"\r\n" + "\r\n\r\n".join([b.to_css(indent + 1) for b in self.nested_blocks])

        return indent_str + css.strip() + f"\r\n{indent_str}}}"

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
    
    def build(self, content_size: int | None = None) -> str:
        imports = ""
        blocks = ""

        for c in self._configs:
            if c.imports:
                imports += "\r\n" + "\r\n".join([i.to_css() for i in c.imports])
            if c.blocks:
                blocks += "\r\n" + "\r\n\r\n".join([b.to_css() for b in c.blocks]) + "\r\n"

        header = f"{ADW_PATCH_HEADER}\r\n{ADW_PATCH_VERSION_HEADER}\r\n"
        content = header + imports + "\r\n" + blocks

        if content_size and len(content) < content_size:
            content += " " * (content_size - len(content))

        return content
    
    def patch(self, target: Path, original: Path):
        content = self.build(content_size=original.stat().st_size)
        target.write_text(content, encoding="utf-8")