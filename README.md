 DHardy's keyboard layouts
=================

Colemak
-----------

What keyboard layout do you use? Standard Qwerty, Dvorak, or something else?
Well, that's your choice, not mine, but if you want a recommendation mine would
be [Colemak](http://colemak.com/). Both Dvorak and Colemak are significantly
more comfortable than Qwerty *for typing*. But maybe there's other things you
do besides typing text: it turns out use of Ctrl+z, Ctrl+x, Ctrl+c and
Ctrl+v (suspend/undo, cut, kill command/copy, paste) are very commonly used on
PCs based on their convenient positions in the Qwerty layout. This (and the
capslock-is-backspace option) is easily the biggest reason not to use Dvorak
(well, assuming you're willing to spend a little time getting used to a new
layout); thankfully Colemak keeps these keys in their Qwerty position.


Colemak + symbol layout
---------------------------------

The above explains why I use Colemak, but not what these files are. After a
while I found Colemak really nice for typing on, but found myself always
reaching for various symbols in wierd positions on the number row while
programming. I write quite a bit of code:

    x := 2*3
    vec := { 1, 2, 3 }
    // oh, and real operators:
    x ∉ vec
    (x ÷ 3) ∈ vec

that type of thing. Colemak may have made English text a lot nicer to type, but
code symbols could still be massively easier to type. Of course, the best keys
on the keyboard are already taken — we use them for typing letters, not
numbers, operators and other symbols. I took my inspiration from the
[neo](http://www.neo-layout.org/) layout: use an extra shift key. It turns out
that XKB (the linux keyboard layout system) has good support for 4 levels of
input per key (unshifted, with shift, with alt, with alt+shift). It even
supports 8 levels per key (I think this is mainly used in Cyrillic languages).
So all I had to do was activate a second shift key, and add some symbols to the
other keys. Oh, and design a keyboard layout.


The layout
--------------

I'll copy and paste my charts from the 'cyborg16' XKB file. They're designed to
be read with a fixed-width font, so if the lines don't match up you'd better
find some other way of viewing the tables.

    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ ` ┊ 1 ┊ 2 ┊ 3 ┊ 4 ┊ 5 ┊ 6 ┊ 7 ┊ 8 ┊ 9 ┊ 0 ┊ - ┊ = ┊ BckSp ┃
    ┃ Tab ┊ q ┊ w ┊ f ┊ p ┊ g ┊ j ┊ l ┊ u ┊ y ┊ ' ┊ ö ┊ ü ┊  \  ┃
    ┃ BkSp ┊ A ┊ R ┊ S ┊ T ┊ d ┊ h ┊ N ┊ E ┊ I ┊ O ┊ ä ┊  Enter ┃
    ┃ Shift  ┊ z ┊ x ┊ c ┊ v ┊ b ┊ k ┊ m ┊ , ┊ . ┊ / ┊  Shift   ┃
    ┃Fn ┊Ctrl┊Wn┊Alt┊ Space              ┊Alt┊Mnu┊Ctl┊  Arrows  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ ~ ┊ ! ┊ @ ┊ # ┊ $ ┊ % ┊ ^ ┊ & ┊ * ┊ ( ┊ ) ┊ _ ┊ + ┊ BckSp ┃
    ┃ Tab ┊ q ┊ w ┊ f ┊ p ┊ g ┊ j ┊ l ┊ u ┊ y ┊ " ┊ Ö ┊ Ü ┊  |  ┃
    ┃ BkSp ┊ A ┊ R ┊ S ┊ T ┊ d ┊ h ┊ N ┊ E ┊ I ┊ O ┊ Ä ┊  Enter ┃
    ┃ Shift  ┊ z ┊ x ┊ c ┊ v ┊ b ┊ k ┊ m ┊ ; ┊ : ┊ ? ┊  Shift   ┃
    ┃Fn ┊Ctrl┊Wn┊Alt┊ Space              ┊Alt┊Mnu┊Ctl┊  Arrows  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃`èù┊´éú┊¨ëü┊ £ ┊ € ┊ ¤ ┊^¹û┊¯ēū┊ · ┊˘ĕŭ┊   ┊ − ┊ ≡ ┊ BckSp ┃
    ┃ Tab ┊ < ┊ { ┊ / ┊ | ┊ % ┊ ^ ┊ & ┊ * ┊ } ┊ > ┊ é ┊ è ┊  #  ┃
    ┃ BkSp ┊ [ ┊ ( ┊ - ┊ ! ┊ 0 ┊ 1 ┊ = ┊ + ┊ ) ┊ ] ┊ à ┊  Enter ┃
    ┃ Shift  ┊ ` ┊ " ┊^¹û┊ $ ┊ \ ┊ _ ┊ — ┊ ; ┊ : ┊ # ┊  Shift   ┃
    ┃Fn ┊Ctrl┊Wn┊Alt┊ _                  ┊Alt┊Mnu┊Ctl┊  Arrows  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ ‘ ┊ ’ ┊ “ ┊ ” ┊ ¢ ┊   ┊   ┊ ÷ ┊ × ┊   ┊   ┊ — ┊ ± ┊ BckSp ┃
    ┃ Tab ┊ ≤ ┊   ┊ ÷ ┊ √ ┊   ┊^¹û┊   ┊ × ┊   ┊ ≥ ┊ É ┊ È ┊     ┃
    ┃ BkSp ┊ ∉ ┊ ∈ ┊ ß ┊   ┊   ┊   ┊ ≡ ┊ + ┊ ∋ ┊ ∌ ┊ À ┊  Enter ┃
    ┃ Shift  ┊   ┊   ┊ ç ┊^¹û┊   ┊   ┊ µ ┊ « ┊ » ┊ ¿ ┊  Shift   ┃
    ┃Fn ┊Ctrl┊Wn┊Alt┊ _                  ┊Alt┊Mnu┊Ctl┊  Arrows  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

The four diagrams show, in order, the unshifted glyphs, the shifted (capital)
layer, the symbol layer, and the additional symbol/international layer. If
you're a bit confused by the `' ä ö ü à é è` keys on the right, these are my
modified swiss layout. Don't worry, there are other variants if you don't need
the german/french letters.

Variants of the layout:

*   **colemak** — US keyboard, colemak layout and progsyms
*   **colemak_ch** — US keyboard, colemak layout, Swiss-inspired accented keys
    and progsyms
*   **colemak_ukch** — UK keyboard, colemak layout, near-Swiss accented keys,
    and progsyms
*   **dvorak_uk** — UK keyboard, Dvorak layout and progsyms
*   **basic** (default variant) — US keyboard, qwerty layout and progsyms
*   **basic_uk** — UK keyboard, qwerty layout and progsyms

Other variants are quite easy to think of, but since near limitless
combinations are possible defining other variants is left as an exercise to the
reader (see the section below on customising the layout).


Installation on linux
--------------------------

Installation consists of three steps:

1.  install the layout file
2.  make graphical configuration tools aware of the new layout and variants
    (optional)
3.  set the layout and a third-level modifier key

The first step is very easy: copy the layout file into the XKB layouts
directory. Assuming this has the same location on your system as debian (and
probably Ubuntu):

    sudo cp cyborg16 /usr/share/X11/xkb/symbols/

### Making your desktop environment aware of the new layout

As soon as you've done this, you can go ahead and call `setxkbmap` (below). But
if you want to set the layout from the Gnome/KDE settings panel, you need to
perform an extra step to tell the GUI about the new layout.

To do this, open the rules/base.xml file in a text editor:

    sudo cp /usr/share/X11/xkb/rules/base.xml \
        /usr/share/X11/xkb/rules/base.xml.bak
    sudoedit /usr/share/X11/xkb/rules/base.xml

(if the above doesn't work, try [setting your EDITOR or VISUAL environment
variable](http://en.wikibooks.org/wiki/Guide_to_Unix/Environment_Variables)
first: `export VISUAL=kwrite` or whatever).

This file is quite big and has three sections:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xkbConfigRegistry SYSTEM "xkb.dtd">
<xkbConfigRegistry>
  <modelList>
    ...
  </modelList>
  <layoutList>
    ...
  </layoutList>
  <optionList>
    ...
  </optionList>
</xkbConfigRegistry>

Find the end of the `layoutList` section and insert the contents of the
[cyborg16-base.xml-extension][] file there (just before `</layoutList>`. Make
sure the XML is valid (each opening `<tag>` has a corresponding closing
`</tag>`). Save the file and close the editor (necessary for sudoedit to update
the original), then log out and log back in (or restart). [I'm not entirely sure
logging out and back in is necessary. Maybe it's only necessary to (close and
freshly) start the keyboard layout configuration.]

### Setting the layout

#### From your desktop environment

If you successfully ammended the base.xml file as documented above, you should
be able to use the Gnome/KDE settings panels to change the keyboard
layout.

Note that this method does have a (dis)advantage: settings are only applied
after logging in. This means you have to remember which layout you're using when
giving gdm/kdm your password — fun.

#### From the command-line

To set the layout from the command-line, use `setxkbmap`:

    setxkbmap cyborg16
    # or
    setxkbmap cyborg16 colemak

If you want to use a different variant, you can specify that too. You can also
specify the keyborad model and extra options. I use the following (note that
the layout is provided twice with two variants: `colemak_ch` is the default,
and `basic` (qwerty) is the alternative layout — the `grp:sclk_toggle` option
allows me to change between these by pressing the scroll-lock button):

    setxkbmap -layout cyborg16,cyborg16 -variant colemak_ch,basic -option \
        -option grp:sclk_toggle,grp_led:caps,compose:menu,caps:backspace \
        -model thinkpad60

Note that you might also need to set the second modifier key used to access the
third and forth levels of the layout; I use the right alt key, which is
sometimes labelled AltGr (short for alternate graphic). Depending on your
physical keyboard this may not seem massively comfortable to press all the
time, but I soon found I got used to this — it's simply using your thumb in a
way you're not used to using it.

#### Making your changes permanent

The keyboard layout used to be set in `xorg.conf`. Maybe it still can be set
there (I haven't tried recently), but (in debian linux at least) the layout is
normally set in `/etc/default/keyboard`. Run

    sudoedit /etc/default/keyboard

and change the `XKBLAYOUT` and optionally other lines. My file includes the
following:

    XKBMODEL="thinkpad60"
    XKBLAYOUT="cyborg16"
    XKBVARIANT="colemak_ch"
    XKBOPTIONS="grp:sclk_toggle,grp_led:caps,compose:menu,caps:backspace"

After this change, linux should use the new layout for all users on boot
(but note that desktop environment settings may override the system layout once
a user logs in).


Installing on other systems
----------------------------------

The included rules are intended for XKB. If you're using Windows or Mac OS X
you'll have to find out how to customise keyboard layouts and write your own
rules. Please do share if you do this; I'm sure it's possible though I don't
know how (maybe looking at the [colemak](http://colemak.com/) installer would
help you get started).


Customising the layout
------------------------------

If you want to modify the layout, go ahead and modify the cyborg16 file. To
keep things tidy, I suggest you only put symbols in the "prog_intl" section
and create a new section if you want a different base keyboard variant. You can
find names for several symbols in the international-symbols.txt file, and may
want to edit the XML chunk in cyborg16-base.xml-extension if you create a new
variant.

Terminology and syntax: everything in the cyborg16 file defines XKB's cyborg16
*layout*. Each section in the file defines a new *variant*; the default
*variant* is called "basic". The command `include "us(dvorak)"` means import
the rules of the **dvorak** *variant* of the **us** *layout*.
