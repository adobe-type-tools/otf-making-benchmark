# OTF Making Benchmark

The purpose of this repository is to serve as a test case for comparing an OpenType (.otf)
font built with the [AFDKO](http://www.adobe.com/devnet/opentype/afdko.html)'s **makeotf**
tool, with another font built with **[fontmake](https://github.com/googlei18n/fontmake)**
from the same source files.

The font source files in this repository are a simplified version of
[Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro) Regular. When processed
with **makeotf**, these files should produce an OpenType-CFF font that is very similar to
[version 2.020](https://github.com/adobe-fonts/source-sans-pro/releases/tag/2.020R-ro%2F1.075R-it),
with one significant different: the font made from this repository will not be autohinted.


### Requirements

* [makeotf](https://github.com/adobe-type-tools/afdko/releases/latest)
* [fontmake](https://github.com/googlei18n/fontmake)


### Building the fonts

To build the font with **makeotf** use this command:
```sh
sh buildSans-makeotf.sh
```

And to build the font with **fontmake** use this command:
```sh
sh buildSans-fontmake.sh
```

### Current status
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
