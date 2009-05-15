AC_PREREQ(2.53)

AC_INIT([moblin-icon-theme], [0.1])
AC_CONFIG_SRCDIR([16x16])

AM_INIT_AUTOMAKE([1.9 tar-ustar])

# Define the toplevel path here
AC_SUBST(themedir, "\${datadir}/icons/")

UTILS_REQUIRED=0.8.7

AC_MSG_CHECKING([icon-naming-utils >= $UTILS_REQUIRED])
PKG_CHECK_EXISTS(icon-naming-utils >= $UTILS_REQUIRED,
                 have_utils=yes, have_utils=no)
if test "x$have_utils" = "xyes"; then
   UTILS_PATH="`$PKG_CONFIG --variable=program_path icon-naming-utils`"
   ICONMAP="$UTILS_PATH/icon-name-mapping"
   AC_SUBST(ICONMAP)
   AC_MSG_RESULT([yes])
else
   AC_MSG_RESULT([no])
   AC_MSG_ERROR([icon-naming-utils >= $UTILS_REQUIRED is required to build
                 and install sato-icon-theme])
fi


AC_CONFIG_FILES([
Makefile

16x16/Makefile
16x16/actions/Makefile
16x16/animations/Makefile
16x16/apps/Makefile
16x16/categories/Makefile
16x16/devices/Makefile
16x16/emblems/Makefile
16x16/emotes/Makefile
16x16/mimetypes/Makefile
16x16/places/Makefile
16x16/status/Makefile
24x24/Makefile
24x24/actions/Makefile
24x24/animations/Makefile
24x24/apps/Makefile
24x24/categories/Makefile
24x24/devices/Makefile
24x24/emblems/Makefile
24x24/emotes/Makefile
24x24/mimetypes/Makefile
24x24/places/Makefile
24x24/status/Makefile
32x32/Makefile
32x32/actions/Makefile
32x32/animations/Makefile
32x32/apps/Makefile
32x32/categories/Makefile
32x32/devices/Makefile
32x32/emblems/Makefile
32x32/emotes/Makefile
32x32/mimetypes/Makefile
32x32/places/Makefile
32x32/status/Makefile
48x48/Makefile
48x48/actions/Makefile
48x48/apps/Makefile
48x48/categories/Makefile
48x48/devices/Makefile
48x48/emblems/Makefile
48x48/emotes/Makefile
48x48/mimetypes/Makefile
48x48/places/Makefile
48x48/status/Makefile
64x64/Makefile
64x64/actions/Makefile
64x64/apps/Makefile
64x64/categories/Makefile
64x64/devices/Makefile
64x64/emblems/Makefile
64x64/emotes/Makefile
64x64/mimetypes/Makefile
64x64/places/Makefile
64x64/status/Makefile
autom4te.cache/Makefile
moblin-icon-theme-0.1/Makefile
moblin-icon-theme-0.1/16x16/Makefile
])

AC_OUTPUT
