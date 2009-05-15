themedir = $(datadir)/icons/Moblin Netbook/32x32/places
theme_DATA = folder.png folder-remote.png folder-saved-search.png inbox.png network-server.png network-workgroup.png start-here.png user-desktop.png user-home.png user-trash.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c places )
MAINTAINERCLEANFILES = Makefile.in
