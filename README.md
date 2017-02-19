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
sh buildFont-makeotf.sh
```

And to build the font with **fontmake** use this command:
```sh
sh buildFont-fontmake.sh
```

### Current status
```
+---+-------------------------+-----------+-----------------+--------------+
| # | File name               | File size |    Size diff    | Font version |
+---+-------------------------+-----------+-----------------+--------------+
| 1 | SourceSans-makeotf.otf  |   185332  |        -        |    2.020     |
| 2 | SourceSans-fontmake.otf |   250628  | 65296 (+35.23%) |    2.020     |
+---+-------------------------+-----------+-----------------+--------------+
+------+--------+------------------+
| Tag  | Font 1 |      Font 2      |
+------+--------+------------------+
| CFF  |  76182 | +18023 (+23.66%) |
| GPOS |  66070 | +51974 (+78.67%) |
| GSUB |  15450 | -2914 (-18.86%)  |
| cmap |  13918 |  -722 (-5.19%)   |
| hmtx |   7768 |        0         |
| name |   4425 |  -870 (-19.66%)  |
| GDEF |    962 |  -162 (-16.84%)  |
| OS/2 |     96 |        0         |
| BASE |     70 |        0         |
| head |     54 |        0         |
| hhea |     36 |        0         |
| post |     32 |        0         |
| DSIG |      8 |       n/a        |
| maxp |      6 |        0         |
+------+--------+------------------+
```
