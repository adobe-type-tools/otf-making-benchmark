#!/bin/sh
fontmake -u Regular/font.ufo -o otf --production-names
mv master_otf/SourceSansPro-Regular.otf SourceSans-fontmake.otf
rm -r master_otf
