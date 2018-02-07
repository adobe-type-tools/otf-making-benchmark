# OTF Making Benchmark

The purpose of this repository is to serve as a test case for comparing OpenType (.otf)
fonts built with the [AFDKO](https://github.com/adobe-type-tools/afdko)'s **makeotf**
tool, with fonts built with **[fontmake](https://github.com/googlei18n/fontmake)**
from the same source files.

The font source files in this repository are a simplified version of,
* [Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro) Regular
* [Source Serif Pro](https://github.com/adobe-fonts/source-serif-pro) Regular

When processed with **makeotf**, these files should produce OpenType-CFF fonts that are very similar
to [version 2.020](https://github.com/adobe-fonts/source-sans-pro/releases/tag/2.020R-ro%2F1.075R-it),
and [version 1.017](https://github.com/adobe-fonts/source-serif-pro/tree/1.017R) respectively,
with one significant different: the fonts made from this repository will not have hints.


### Requirements

* [makeotf](https://pypi.python.org/pypi/afdko)
* [fontmake](https://pypi.python.org/pypi/fontmake)


### Building the fonts

To build Source Sans with **makeotf** use this command:
```sh
sh buildSans-makeotf.sh
```

And to build Source Sans with **fontmake** use this command:
```sh
sh buildSans-fontmake.sh
```

### Current status

#### Source Sans
```
+---+-------------------------+-----------+-----------------+--------------+
| # | File name               | File size |    Size diff    | Font version |
+---+-------------------------+-----------+-----------------+--------------+
| 1 | SourceSans-makeotf.otf  |   186400  |        -        |    2.045     |
| 2 | SourceSans-fontmake.otf |   236924  | 50524 (+27.11%) |    2.045     |
+---+-------------------------+-----------+-----------------+--------------+
+------+--------+------------------+
| Tag  | Font 1 |      Font 2      |
+------+--------+------------------+
| CFF  |  78029 |  +3282 (+4.21%)  |
| GPOS |  66070 | +51974 (+78.67%) |
| GSUB |  15450 | -2910 (-18.83%)  |
| cmap |  13918 |  -722 (-5.19%)   |
| hmtx |   7768 |        0         |
| name |   3671 |  -930 (-25.33%)  |
| GDEF |    962 |  -162 (-16.84%)  |
| OS/2 |     96 |        0         |
| BASE |     70 |        0         |
| head |     54 |        0         |
| hhea |     36 |        0         |
| post |     32 |        0         |
| maxp |      6 |        0         |
+------+--------+------------------+
```

#### Source Serif
```
+---+--------------------------+-----------+--------------+--------------+
| # | File name                | File size |  Size diff   | Font version |
+---+--------------------------+-----------+--------------+--------------+
| 1 | SourceSerif-fontmake.otf |   68592   |      -       |    1.017     |
| 2 | SourceSerif-makeotf.otf  |   69408   | 816 (+1.19%) |    1.017     |
+---+--------------------------+-----------+--------------+--------------+
+------+--------+----------------+
| Tag  | Font 1 |     Font 2     |
+------+--------+----------------+
| CFF  |  27708 | -1930 (-6.97%) |
| GPOS |  24220 | +220 (+0.91%)  |
| name |  10706 | +957 (+8.94%)  |
| hmtx |   2188 |       0        |
| GSUB |   1876 | +886 (+47.23%) |
| cmap |   1398 | +680 (+48.64%) |
| OS/2 |     96 |       0        |
| BASE |     58 |       0        |
| head |     54 |       0        |
| hhea |     36 |       0        |
| post |     32 |       0        |
| maxp |      6 |       0        |
+------+--------+----------------+
```
