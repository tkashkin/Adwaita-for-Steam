#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

ADW_REQUIRED_PYTHON_VERSION = (3, 11)
if sys.version_info < ADW_REQUIRED_PYTHON_VERSION:
    sys.exit("Adwaita-for-Steam installer requires Python %s.%s or later" % ADW_REQUIRED_PYTHON_VERSION)

from scripts.installer.installer import AdwInstaller

if __name__ == "__main__":
    AdwInstaller()