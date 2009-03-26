#! /bin/bash

if [ "x$1" = "x" ]
then
  echo "Usage: $0 [icon theme directory]"
  exit 1
fi

THEME_NAME="$1"
THEME_COMMENT="$THEME_NAME Icon Theme"

cd "$1"

echo "Creating icon theme in '$1'"

echo "Creating index.theme"

echo -e "[Icon Theme]\nName=$THEME_NAME\nComment=$THEME_COMMENT\n" > index.theme
echo -n "Directories=" >> index.theme

DIRS=`find * -type d | grep -v git | grep -v scalable | grep "/"`

for foo in $DIRS
do
	echo -n "$foo," >> index.theme
done

for foo in $DIRS
do
	echo -en "\n\n[$foo]\nSize=`echo $foo | sed 's/\x.*//'`\nContext=`basename $foo`\nType=Fixed" >> index.theme
done


echo "Creating Makefiles"

subdirs="actions apps devices status places mimetypes stock"

SIZES=$(find * -maxdepth 0 -type d -printf '%f ')

for dir in $SIZES
do
  subdirs=$(find $dir/* -maxdepth 0 -type d -printf '%f ')
  echo "SUBDIRS=$subdirs" > $dir/Makefile.am

              for context in $subdirs
              do
                      files=`echo $dir/$context/*.png|sed "s/$dir\/$context\///g"`
                      echo "themedir = \$(datadir)/icons/Sato/$dir/$context" > $dir/$context/Makefile.am
                      echo "theme_DATA = $files" >> $dir/$context/Makefile.am
                      echo "EXTRA_DIST = \$(theme_DATA)" >> $dir/$context/Makefile.am
                      echo "install-data-local: install-themeDATA"  >> $dir/$context/Makefile.am
                      echo "	(cd \$(DESTDIR)\$(themedir) && \$(ICONMAP) -c $context )" >> $dir/$context/Makefile.am
                      echo "MAINTAINERCLEANFILES = Makefile.in" >> $dir/$context/Makefile.am
              done
done

echo "Done"
