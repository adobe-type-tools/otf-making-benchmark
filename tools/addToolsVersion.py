#!/usr/bin/env python

import os
import sys
from fontTools.ttLib import TTFont

__doc__="""\
Adds a string to a font's name ID 10.

Usage:
  python addToolsVersion.py <font> <string>

"""

def run():
	path = os.path.abspath(sys.argv[1])
	string = unicode(str(sys.argv[2]), "utf-8")

	font = TTFont(path)
	font['name'].setName(string, 10, 3, 1, 0x409)
	font['name'].setName(string, 10, 1, 0, 0)
	font.save(path)


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(__doc__)
	else:
		run()
