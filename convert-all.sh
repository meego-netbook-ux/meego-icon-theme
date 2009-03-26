#!/bin/sh

# (c) 2009, Intel
# Author: Hylke Bons <hylke.bons@intel.com>
# This script requires ImageMagick to be installed.

echo ""
echo "Converting \"Moblin Netbook\""

cd Moblin\ Netbook
./convert.sh

cd ../

echo ""
echo "Converting \"Moblin Netbook White\""
echo ""

cd Moblin\ Netbook\ White/
./convert-white.sh

cd ../

echo "All done."
echo ""
