#! /bin/sh
#
#
install --mode=755 -D src/baxc.py  /usr/share/gnome-baxc/baxc.py
install --mode=755 -D src/gui.py  /usr/share/gnome-baxc/gui.py
install --mode=755 -D src/imagepro.py  /usr/share/gnome-baxc/imagepro.py
install --mode=755 -D src/xmlmsg.py  /usr/share/gnome-baxc/xmlmsg.py
install --mode=755 -D gnome-baxc.svg /usr/share/icons/hicolor/scalable/apps/gnome-baxc.svg
install -D src/Gnome-Baxc.desktop /usr/share/applications/Gnome-Baxc.desktop
install --mode=755 -D gnome-baxc  /usr/bin/gnome-baxc
xdg-icon-resource forceupdate --theme hicolor &>/dev/null
update-desktop-database -q
