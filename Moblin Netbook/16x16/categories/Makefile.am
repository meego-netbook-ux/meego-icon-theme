themedir = $(datadir)/icons/Moblin Netbook/16x16/categories
theme_DATA = applications-accessories.png applications-development.png applications-games.png applications-graphics.png applications-internet.png applications-multimedia.png applications-office.png applications-other.png applications-system.png preferences-desktop-peripherals.png preferences-desktop.png preferences-system.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c categories )
MAINTAINERCLEANFILES = Makefile.in
