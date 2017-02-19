#!/usr/bin/env python

from __future__ import print_function, division
import os
import sys
from fontTools.ttLib import TTFont

__doc__="""\
Prints a report of the file size and table size differences between two or more fonts.

Usage:
  python fontSizeDiff.py <font1> [<font2> ...]

"""

class FontInfo(object):

	def __init__(self, path):
		self.size = os.path.getsize(path)
		self.name = os.path.basename(path)
		self.version = ''
		self.tables = {}
		self._getTables(path)

	def _getTables(self, path):
		""" Adapted from fontTools.ttx.ttList """
		font = TTFont(path, lazy=True)
		reader = font.reader
		tags = reader.keys()
		for tag in tags:
			entry = reader.tables[tag]
			self.tables[tag] = entry.length
		self.version = "%.3f" % font['head'].fontRevision


def _prefOrder(font):
	return font.size


def printReport(fontsList):
	from prettytable import PrettyTable
	from operator import itemgetter

	# sort the list by font size
	fontsList.sort(key=_prefOrder)

	# --- 1st table ----
	table = PrettyTable(["#", "File name", "File size", "Size diff", "Font version"])
	table.align["File name"] = "l"
	table.padding_width = 1

	for i, font in enumerate(fontsList):
		if i == 0:
			refSize = font.size # record the size of the first font
			sizeDiff = '-'
		else:
			diff = font.size - refSize
			perc = diff / refSize * 100
			sizeDiff = '%s (+%.2f%%)' % (diff, perc)

		table.add_row([i+1, font.name, font.size, sizeDiff, font.version])

	# --- 2nd table ----
	table2 = PrettyTable(["Tag"] + ["Font %s" % (i+1) for i in range(len(fontsList))])
	table2.align["Tag"] = "l"
	table2.align["Font 1"] = "r"
	table2.padding_width = 1

	# establish the row order by reverse-sorting
	# the size of the tables of the 1st font
	sortedTables = sorted(fontsList[0].tables.items(), key=itemgetter(1), reverse=True)
	tableOrder = [x[0] for x in sortedTables]

	for tag in tableOrder:
		rowValues = []
		for i, font in enumerate(fontsList):
			if i == 0:
				refSize = font.tables[tag] # record the size of the first font
				sizeDiff = refSize
			else:
				if tag in font.tables:
					diff = font.tables[tag] - refSize
					if not diff:
						sizeDiff = '0'
					else:
						perc = diff / refSize * 100
						sign = '' if diff < 0 else '+'
						sizeDiff = '%s%s (%s%.2f%%)' % (sign, diff, sign, perc)
				else:
					sizeDiff = 'n/a'

			rowValues.append(sizeDiff)

		table2.add_row([tag] + rowValues)

	print(table)
	print(table2)


def run():
	fontPathsList = [os.path.abspath(path) for path in sys.argv[1:]]

	fontsList = []

	# Collect table sizes & font info
	for path in fontPathsList:
		fontsList.append(FontInfo(path))

	printReport(fontsList)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(__doc__)
	else:
		run()
