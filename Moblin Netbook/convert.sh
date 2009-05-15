#!/bin/sh

# (c) 2009, Intel
# Author: Hylke Bons <hylke.bons@intel.com>
# This script requires ImageMagick an Inkscape to be installed.
# Run in the "Moblin Netbook" directory.

mkdir -p 24x24
mkdir -p 32x32
mkdir -p 48x48
mkdir -p 64x64

echo ""
echo "Exporting icons from source files:"
echo ""

for category in `ls scalable/`; do
  cd scalable/$category
  echo -n "in folder \"$category\""
    for svg in *.svg; do
      base=`echo $svg | sed s/.svg$//`
      mkdir -p ../../48x48/$category/
      mkdir -p ../../64x64/$category/
      convert -background None $svg ../../48x48/$category/$base.png
      inkscape -f $svg -w 64 -h 64 -e ../../64x64/$category/$base.png
      echo -n "."
    done
  cd ../../
  echo " Done."
done


