# Popak romanian keyboard layout installer for Debian
 
A scripted installer for the Romanian Popak keyboard layout http://www.invatasingur.ro/popak/index.php

The author of this layout is Nicolae Popa. I just promised him I would write an installer script for Debian. I started work on this but for now I couldn't finish it because of three things: 1) I'm learning Python 2) I'm new to Debian 3) I'm always tired from work or other obligations and I shamefully can't motivate myself to keep up the work. Fourth would be that I'm afraid to unleash upon the world some script that might break people's operating systems.

I always use this layout when I write in Romanian because I can't write without diacritics anymore. In my opinion,  it's bad style and I usually have negative impressions about people who write in Romanian without diacritics. Every Romanian speaker should write with diacritics otherwise you do injustice to this language. I used the layout screenshots from Mr. Popa's website to learn the keyboard layout. My speed is not too fast but not too slow either, somewhere in between.

I enjoy very much that this is a fully thought keyboard layout, not just some improvisation like the Alt+Key layout, which just makes Romanian seem like a non-important, second level language. Romanian is an important language and it deserves its own full keyboard layout. I'm somehow saddened because so few people write with diacritics in Romanian on the internet and because it doesn't get the attention it deserves with public or governmental institutions.

To switch keyboard layouts in Debian press Win-Key + Space. I think the Win-Key is the Command-Key.


![screenshot](ro-layout-gnome.png)

WORK IN PROGRESS! DON'T RUN THIS YET!
-------------------------------------

I tested these manual steps for Debian 8 Jessie. The installer will do the same, automatically.

## 1) Backup!

Open a terminal as root and

```
# cd /usr/share/X11/xkb/rules
```

Backup the following files:

```
# cp evdev.xml evdev.xml.backup
# cp evdev.lst evdev.lst.backup

# cp base.xml  base.xml.backup
# cp base.xml  base.xml.backup
```

change directory to `symbols`:

```
# cd /usr/share/X11/xkb/symbols
```

and backup this file:

```
# cp ro ro.backup
```
2) Installation 

### evdev.xml

Open the file `/usr/share/X11/xkb/rules/evdev.xml` for editing.

Search for `Romanian (WinKeys)`

You should find something like this:

```
<variant>
  <configItem>
    <name>winkeys</name>
    <description>Romanian (WinKeys)</description>
  </configItem>
</variant>
```

Add the two new variants _Popak (Standard)_ and _Popak (Cedilla)_ right beneath the _Romanian (Winkeys)_ fragment, between the closing tag `</variant>` and `</variantList>`. Make sure that `</variantList>` is under the new Popak variants. It should look like this:

```
  <variant>
    <configItem>
      <name>winkeys</name>
      <description>Romanian (WinKeys)</description>
    </configItem>
  </variant>

  <!-- begin popak -->
  <variant>
    <configItem>
      <name>popak_standard</name>
      <description>Popak (Standard)</description>
    </configItem>
  </variant>
  <variant>
    <configItem>
      <name>popak_cedilla</name>
      <description>Popak (Cedilla)</description>
    </configItem>
  </variant>
  <!-- end popak -->

</variantList> 
```

Save the changes.


### base.xml

Do the same with `/usr/share/X11/xkb/rules/base.xml`.

Remember to save.


### evdev.lst

Open the file `/usr/share/X11/xkb/rules/evdev.lst` for editing.

Search for `Romanian (WinKeys)` again.

You should find something like this:

```
winkeys         ro: Romanian (WinKeys)
```

Add the two _Popak_ lines right beneath the _Romanian (Winkeys)_ line:

```
winkeys         ro: Romanian (WinKeys)
popak_standard  ro: Popak Standard
popak_cedilla   ro: Popak Cedilla
```

Save the changes.


### base.lst

Do the same with `/usr/share/X11/xkb/rules/base.lst`.

Save the changes.


### ro

Open the file `/usr/share/X11/xkb/symbols/ro` for editing.

Search for `xkb_symbols "cedilla"`

You should find something like this:

```
partial alphanumeric_keys
xkb_symbols "cedilla" {
    // Variant of the basic layout with cedillas.
    // Implements S and T with cedilllas as in ISO-8859-2.
    // Included for compatibility reasons (this used to be the def variant).

    include "ro(basic)"

    name[Group1]="Romanian (cedilla)";

    key <AD05> { [ t,                      T,  tcedilla,	 Tcedilla ] };
    key <AC02> { [ s,                      S,  scedilla,	 Scedilla ] };
};
```

Add this block right beneath the one you found:

```
partial default alphanumeric_keys
xkb_symbols "popak_standard" {
// Popak layout, developed by Nicolae Popa (nicolae.m.popa@gmail.com)
// http://www.invatasingur.ro/popak
// Standard variation (with correct diacritics)

    include "us"

    name[Group1]="Romania";

    key <AE01> { [ 1,                 exclam,  section			  ] };
    key <AE02> { [ 2,                     at,  copyright		  ] };
    key <AE03> { [ 3,             numbersign,  guillemotleft 	  	  ] };
    key <AE04> { [ 4,                 dollar,  guillemotright		  ] };
    key <AE05> { [ 5,                percent,  degree			  ] };
    key <AE11> { [ endash,	     	   question			  ] };
    key <AD01> { [ b,                      B,  plusminus		  ] };
    key <AD02> { [ p,                      P,  underscore 	          ] };
    key <AD03> { [ c,                      C,  braceleft  	          ] };
    key <AD04> { [ m,                      M,  braceright		  ] };
    key <AD05> { [ v,                      V,  bar			  ] };
    key <AD06> { [ acircumflex,            Acircumflex			  ] };
    key <AD07> { [ icircumflex,            Icircumflex			  ] };
    key <AD08> { [ abreve,                 Abreve			  ] };
    key <AD09> { [ d,                      D	 			  ] };
    key <AD10> { [ f,                      F	 			  ] };
    key <AD11> { [ w,                      W	 			  ] };
    key <AD12> { [ k,                      K	 			  ] };
    key <AC01> { [ l,                      L,  doublelowquotemark         ] };
    key <AC02> { [ t,                      T,  rightdoublequotemark	  ] };
    key <AC03> { [ r,                      R,  less 			  ] };
    key <AC04> { [ n,                      N,  greater 			  ] };
    key <AC05> { [ s,                      S,  EuroSign 		  ] };
    key <AC06> { [ o,                      O	 			  ] };
    key <AC07> { [ a,                      A	 			  ] };
    key <AC08> { [ e,                      E	 			  ] };
    key <AC09> { [ i,                      I	 			  ] };
    key <AC10> { [ u,                      U	 			  ] };
    key <AC11> { [ z,                      Z	 			  ] };
    key <LSGT> { [ q,            	   Q                              ] };
    key <BKSL> { [ q,            	   Q                              ] };
    key <AB01> { [ y,                      Y,  apostrophe 	       	  ] };
    key <AB02> { [ 0x1000219,      0x1000218,  quotedbl 	       	  ] };
    key <AB03> { [ 0x100021b,      0x100021a,  bracketleft 	       	  ] };
    key <AB04> { [ h,                      H,  bracketright 	       	  ] };
    key <AB05> { [ x,                      X,  backslash 	       	  ] };
    key <AB06> { [ j,                      J		 	       	  ] };
    key <AB07> { [ g,                      G		 	       	  ] };
    key <AB08> { [ comma, 	   semicolon		          	  ] };
    key <AB09> { [ period,             colon 	      		    	  ] };
    key <AB10> { [ minus,              slash 	      		    	  ] };

    include "level3(ralt_switch)"
};

partial alphanumeric_keys
xkb_symbols "popak_cedilla" {
    // Variant of the Popak layout with cedillas.
    // Implements S and T with cedilllas as in ISO-8859-2.
    // Included for compatibility reasons.

    include "ro(popak_standard)"

    name[Group1]="Romania";

    key <AB02> { [ scedilla,      Scedilla,  quotedbl 	       	  	  ] };
    key <AB03> { [ tcedilla,      Tcedilla,  bracketleft 	       	  ] };
};
```

Save the changes.


Reboot
----
