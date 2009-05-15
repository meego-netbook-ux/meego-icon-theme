themedir = $(datadir)/icons/Moblin Netbook/16x16/devices
theme_DATA = audio-card.png audio-input-microphone.png battery.png camera-photo.png camera-video.png computer.png drive-disk.png drive-harddisk.png drive-optical.png drive-removable-media.png input-gaming.png input-keyboard.png input-mouse.png media-flash.png media-floppy.png media-optical.png multimedia-player.png network-wired.png network-wireless.png printer.png video-display.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c devices )
MAINTAINERCLEANFILES = Makefile.in
