themedir = $(datadir)/icons/Moblin Netbook/16x16/emotes
theme_DATA = face-angel.png face-crying.png face-devilish.png face-glasses.png face-grin.png face-kiss.png face-monkey.png face-plain.png face-sad.png face-smile-big.png face-smile.png face-surprise.png face-wink.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c emotes )
MAINTAINERCLEANFILES = Makefile.in
