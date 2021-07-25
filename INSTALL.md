To install, first copy the `cyborg16` file to the `xkb/symbols` dir:
```
sudo cp cyborg16 /usr/share/X11/xkb/symbols/
```

If you're running X11 that's already enough to test; e.g. to set the `basic` variant (under restart or otherwise adjusted):
```
setxkbmap cyborg16 basic
```
But if you're running Wayland that won't do anything.

Now, open `evdev-extension.xml` and copy the contents, then open `xkb/rules/evdev.xml` for editing:
```
VISUAL=kwrite sudoedit /usr/share/X11/xkb/rules/evdev.xml
```
Paste the contents you copied here, under the xpath `/xkbConfigRegistry/layoutList` (i.e. just after `<layoutList>`).

Now, restart the display manager (e.g. `systemctl restart gdm.service`), and the new layouts should show up in your system settings.

Alternative (X11 only): edit the system's default X11 settings under `/etc/default/keymap` or `/etc/X11/xorg.conf.d/00-keyboard.conf` or similar.
