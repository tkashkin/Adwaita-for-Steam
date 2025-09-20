#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

from scripts.installer.installer import AdwInstaller

if __name__ == "__main__":
	AdwInstaller()