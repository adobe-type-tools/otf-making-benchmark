#!/bin/sh
makeotf -f Regular/font.ufo -r
rm Regular/current.fpr
mv Regular/SourceSansPro-Regular.otf SourceSans-makeotf.otf
