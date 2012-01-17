#! /bin/sh
#
#

install --mode=755 -D baxc  /usr/share/gnome-baxc/gnome-baxc
install --mode=755 -D gui.py  /usr/share/gnome-baxc/gui.py
install --mode=755 -D imagepro.py  /usr/share/gnome-baxc/imagepro.py
install --mode=755 -D xmlmsg.py  /usr/share/gnome-baxc/xmlmsg.py
install --mode=755 -D baxc50.png  /usr/share/gnome-baxc/baxc50.png

install -D Gnome-Baxc.desktop /usr/share/applications/Gnome-Baxc.desktop
cp -s  /usr/share/gnome-baxc/gnome-baxc  /usr/bin/gnome-baxc
