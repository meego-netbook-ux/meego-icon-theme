themedir = $(datadir)/icons/Moblin Netbook/64x64/mimetypes
theme_DATA = application-certificate.png application-x-executable.png audio-x-generic.png email.png font-x-generic.png image-x-generic.png package-x-generic.png photo.png podcast.png text-x-generic.png text-x-generic-template.png text-x-html.png video-x-generic.png x-office-address-book.png x-office-calendar.png x-office-document-template.png x-office-drawing.png x-office-drawing-template.png x-office-presentation.png x-office-presentation-template.png x-office-spreadsheet.png x-office-spreadsheet-template.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c mimetypes )
MAINTAINERCLEANFILES = Makefile.in
