themedir = $(datadir)/icons/Moblin Netbook/32x32/animations
theme_DATA = process-working.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c animations )
MAINTAINERCLEANFILES = Makefile.in
