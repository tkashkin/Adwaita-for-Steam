#!/usr/bin/env python3

from abc import ABC, abstractmethod
from argparse import ArgumentParser, _ArgumentGroup, Namespace, RawTextHelpFormatter
from dataclasses import dataclass

from .css import AdwCSSConfig

@dataclass
class AdwParsedOptionGroup(ABC):
    @abstractmethod
    def to_css(self) -> AdwCSSConfig | None:
        return None

class AdwOptionGroup(ABC):
    title: str | None = None
    description: str | None = None

    @abstractmethod
    def add_options(self, args: _ArgumentGroup):
        raise NotImplementedError

    @abstractmethod
    def parse(self, args: Namespace) -> AdwParsedOptionGroup:
        raise NotImplementedError

class AdwArgsParser:
    _parser: ArgumentParser
    _groups: dict[str, AdwOptionGroup]

    def __init__(self, **groups: AdwOptionGroup):
        self._parser = ArgumentParser(
            description="Adwaita-for-Steam installer",
            formatter_class=RawTextHelpFormatter,
            add_help=False
        )
        self._groups = {}
        for key, group in groups.items():
            self.append(key, group)

    def append(self, key: str, group: AdwOptionGroup):
        group.add_options(
            self._parser.add_argument_group(
                title=group.title,
                description=group.description
            )
        )
        self._groups[key] = group

    def parse(self) -> tuple[list[AdwCSSConfig], dict[str, AdwParsedOptionGroup]]:
        args = self._parser.parse_args()
        css = []
        options = {}
        for key, group in self._groups.items():
            parsed = group.parse(args)
            cfg = parsed.to_css()
            if cfg: css.append(cfg)
            options[key] = parsed
        return (css, options)