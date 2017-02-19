#!/usr/bin/env python

from __future__ import print_function
from subprocess import Popen, PIPE


def runCmd(cmd):
	popen = Popen(cmd, stdout=PIPE, shell=True)
	out, _ = popen.communicate()
	if out:
		return out
	return ''


def parseOutput(out, regexp):
	ver = regexp.search(out)
	if ver:
		return list(ver.groups())


def run():
	libs = [
		'booleanOperations',
		'compreffor',
		'cu2qu',
		'defcon',
		'fontmake',
		'fontMath',
		'fonttools',
		'glyphsLib',
		'MutatorMath',
		'pyclipper',
		'ufo2ft',
		'ufoLib',
		]

	out = runCmd('pip freeze')

	for item in out.splitlines():
		lib, ver = item.split('==')
		if lib not in libs:
			continue
		if lib == 'booleanOperations':
			lib = 'boolOps'
		print('%-12s' '%s' % (lib, ver))


if __name__=='__main__':
	run()
