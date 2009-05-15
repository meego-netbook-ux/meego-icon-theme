themedir = $(datadir)/icons/Moblin Netbook/48x48/devices
theme_DATA = audio-card.png audio-input-microphone.png battery.png bluetooth.png camera-photo-dslr.png camera-photo.png camera-video.png computer.png drive-harddisk.png drive-optical.png drive-removable-media.png gaming-ps3.png gaming-xbox360.png input-gaming.png input-keyboard.png input-mouse.png iphone.png media-flash.png media-floppy.png media-optical.png multimedia-player-ipod.png multimedia-player.png network-wired.png network-wireless.png phone-cell.png printer.png projecter.png projector.png radio.png television.png usb.png video-display.png
EXTRA_DIST = $(theme_DATA)
install-data-local: install-themeDATA
	(cd "$(DESTDIR)$(themedir)" && $(ICONMAP) -c devices )
MAINTAINERCLEANFILES = Makefile.in
