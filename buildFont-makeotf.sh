#!/usr/bin/env sh

makeotf -f Regular/font.ufo -r -omitDSIG
mv Regular/SourceSansPro-Regular.otf SourceSans-makeotf.otf

# print tools version to stdout and
# add the info to the font's name ID 10
if [[ $1 = "-v" ]]; then
	echo
	versions=`python tools/getMakeotfVersions.py`
	echo "$versions"
	python tools/addToolsVersion.py SourceSans-makeotf.otf "$versions"
fi
