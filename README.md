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
**NOTE:** Currently it requires this change https://github.com/googlei18n/ufo2ft/pull/110
```sh
sh buildFont-fontmake.sh
```
