#!/usr/bin/env python3

from pathlib import Path
import shutil

from .log import *

def copy_dir(source: Path, target: Path):
    if not source.is_dir():
        critical(f"copy_dir: {source} is not a valid directory")
    if target.is_dir():
        shutil.rmtree(target)
    shutil.copytree(source, target)

def copy_file(source: Path, target: Path):
    if not source.is_file():
        critical(f"copy_file: {source} is not a valid file")
    shutil.copy(source, target)

def write_text(target: Path, content: str, append: bool = False):
    with target.open("a" if append else "w", encoding="utf-8") as file:
        file.write(content)