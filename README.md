DHardy's keyboard layouts
=================

There are two parts here: a Colemak advertisement and shortcuts for entering
various symbols easily (things like `{`, `≤`, `∈`, `ç`). Skip down a bit if
you're only interested in the latter!


Colemak
-----------

What keyboard layout do you use? Standard Qwerty, Dvorak,
[neo](http://neo-layout.org/), [Colemak](http://colemak.com/), or something
else?

I see only two reasons for abandoning Qwerty:

+   Ease of typing. I haven't used neo, but both Colemak and Dvorak, after
    fingers become used to the new workloads, are significantly more
    comfortable to type on than Qwerty ever was. (This will probably lead to
    lower error rates _and_ higher speeds when proficient, by the way.)
+   Ease of entering symbols. Want to use signs like ÷, £, ä, → and ≠? Most of
    these have been available in some keyboard layouts for a long time, and
    others not too hard to enter anyway (e.g. compose+`-`+`>` yields `→` on
    linux), but they could be easier, especially characters like ä, ö, ü (or
    à, é, è, depending on language).
    
    My original reason, though, for customising keyboard layouts, is because,
    programming, I want to write things like
    `while( list[i] != 0 ){ sum += list[i]; ++i; }` a lot. Not having to grope
    for +, { and ! from difficult-to-reach positions is much nicer.

Whichever your reason for switching, you should bear another factor in mind:
practicality. Consider:

+   Shortcuts. Ctrl+C and Ctrl+Z are very common shortcuts — probably used more
    than 'z' and 'c' are entered themselves. Although you _could_ change the
    bindings in most applications to use the same physical keys, this isn't so
    convenient and doesn't always work expectedly; for this reason I don't
    recommend Dvorak or neo.
+   Can you use your layout on most machines? Unlike Dvorak, neo and standard
    Colemak, my layout is only available for linux and only where you can
    convince the administrator to install the layout.


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

that type of thing.

Colemak was designed to make English text easier to write; the author didn't
try to optimise the positions of symbols. In fact, other than moving the
semicolon/colon key, all symbol keys were left untouched to make colemak easier
to learn. With that in mind, it shouldn't be surprising to find that someone
tries to optimise symbol keys (indeed if you read through the colemak forums,
you will find several other such attempts).

So what was my approach? Of course, the best keys on the keyboard are already
taken — we use them for typing letters, not numbers, operators and other
symbols. I took my inspiration from the [neo](http://www.neo-layout.org/)
layout: use an extra shift key. It turns out that XKB (the linux keyboard layout
system) has good support for 4 levels of input per key (unshifted, with shift,
with alt, with alt+shift). It even supports 8 levels per key (I think this is
mainly used in Cyrillic languages). So all I had to do was activate a second
shift key, and add some symbols to the other keys. Oh, and design a keyboard
layout.


The layout
--------------

Have a look here:
[cyborg16](https://github.com/dhardy/keyboard/blob/master/cyborg16)


### Variants of the layout

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

### Why this layout in particular?

Quite a bit of thought and time has gone into creating this layout.

+   I started the design on the basis that a symmetrical layout (each key on the
left hand corresponding to a related/opposite key on the right hand) would make
it easier to remember. If you look at the operators and the brackets in
particular you should be able to spot this symmetry; unfortunately there was no
obvious way to apply this to all keys and still fit all the symbols I wanted in,
hence the bottom row is rather a jumble.
+   The design tries to make nearly all symbols you might want to use available
on the standard 3 rows of the keyboard. Numbers (other than the frequently used
0 and 1) are left on the top row since they're not so difficult to access from
there.
+   I have "evolved" the design over time: every so often deciding *such and
such* would be better *there* and *another key* could be placed *over there*.
Unlike [carpalx](http://mkweb.bcgsc.ca/carpalx/?home) it's not
computer optimised — it's *me optimised* to be easy to remember and comfortable
to type on (I saw no obvious way to formalise comfort and memorability, and
wasn't really convinced that the methods used in the carpalx generator took
everything necessary into account).

So is this layout well optimised in general or more importantly for *your*
usage? The answer isn't obvious (but most likely the answer is **no**: a more
optimal layout could be found). However concentrating solely on whether or not
this is the **best** layout is somewhat missing the point: the question you are
probably asking is *is it worth me learning?* Of course, I cannot answer that
for you, but I can tell you I find this layout a *massive* improvement over
standard qwerty or colemak, not just for programming but also for writing plain
text.


Symbols via sequences (compose)
-----------------------------

Symbols can also be entered using sequences: `compose` + `-` + `>` maps to `→`,
for example. Many of these are available by default on linux; I've added a few
more combinations like `compose` + `f` + `a` producing `∀`.

If you're wondering what compose is or how to enable it, see
[https://help.ubuntu.com/community/ComposeKey]() (or just add
`compose:menu` to your XKB options).

To use my extensions, copy or link the file `XCompose` to `$HOME/.XCompose` and
restart applications. (For GTK applications I think some additional hack is
necessary.)


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

#### Dealing with modified layout files

It appears that keymaps are compiled by xkbcomp and compiled versions are 
stored in /var/lib/xkb . If there is already a compiled keymap, it appears that 
it will be loaded. To use the latest version, you can either use setxkbmap via 
xkbcomp:

    setxkbmap ... -print | xkbcomp - $DISPLAY

(this is not a good solution as it appears the compiled maps still get used 
on hotloading) or you can delete the files in /var/lib/xkb to force the 
compiled maps to be regenerated (still investigating whether this is a good 
solution).


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
