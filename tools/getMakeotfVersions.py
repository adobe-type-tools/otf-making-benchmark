#!/usr/bin/env python

from __future__ import print_function
import re
from subprocess import Popen, PIPE


re_makeotf  = re.compile(r'(makeotf)\s+v([0-9.]+)', re.DOTALL)
re_mkotfexe = re.compile(r'(makeotf.lib)\s+version:\s+([0-9.]+)(\s+OTF Library) Version:\s+([0-9]+)', re.DOTALL)
re_tx       = re.compile(r'(    tx[\s\S]+)', re.DOTALL)


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
	commands = [
		'makeotf -u',
		'makeotfexe -u',
		'tx -v',
		]
	regexps = [
		re_makeotf,
		re_mkotfexe,
		re_tx
		]

	verStr = ''
	for i, cmd in enumerate(commands):
		out = runCmd(cmd)
		verStr += ' '.join(parseOutput(out, regexps[i])) + '\n'

	verStr = verStr.replace('OTF Library', 'OTF_Library').strip()
	for item in verStr.splitlines():
		line = item.strip()
		s1, s2 = line.split()
		# http://stackoverflow.com/questions/35236759/python-print-in-two-columns
		print('%-12s' '%s' % (s1, s2))


if __name__=='__main__':
	run()
