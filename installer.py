import fileinput
import logging
import logging.config
from shutil import copy2

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('installer')

# constants ------------------------------------------------------

DIR_RULES = 'original/usr/share/X11/xkb/rules/'
DIR_SYMBOLS = 'original/usr/share/X11/xkb/symbols/'

RULES_BASE_XML = DIR_RULES + 'base.xml'
RULES_BASE_LST = DIR_RULES + 'base.lst'

RULES_EVDEV_XML = DIR_RULES + 'evdev.xml'
RULES_EVDEV_LST = DIR_RULES + 'evdev.lst'

SYMBOLS_RO = DIR_SYMBOLS + 'ro'
EXT_BACKUP = '.backup'

XML_FRAGMENT = '''        <variant>
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
'''

LST_FRAGMENT = '''  popak_standard  ro: Popak Standard
  popak_cedilla   ro: Popak Cedilla
'''

SYMBOLS_RO_FRAGMENT = '''
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

'''

# methods --------------------------------------------------------

def backup(file):
    file_backup = file + EXT_BACKUP
    logging.debug('creating backup for ' + file + ' -> ' + file_backup)
    # copy2(src,dst)
    copy2(file, file_backup)


def match_replace(file_path, signal_str, append_to_str, replace_str):
    match = False
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            if signal_str in line:
                match = True
            if match:
                if append_to_str in line:
                    line = line.replace(line, line + replace_str)
                    # logger.debug(line)
                    print(line, end='')
                    match = False
                else:
                    print(line, end='')
            else:
                print(line, end='')


# installation logic ---------------------------------------------

# TODO: detect already installed popak and stop
# TODO: backup incremental if .backup already exists -> .backup2

# backup(RULES_BASE_XML)
# backup(RULES_BASE_LST)

# backup(RULES_EVDEV_XML)
# backup(RULES_EVDEV_LST)

# backup(SYMBOLS_RO)


# match_replace(RULES_EVDEV_XML, 'Romanian (WinKeys)', '</variant>', XML_FRAGMENT)
# match_replace(RULES_BASE_XML, 'Romanian (WinKeys)', '</variant>', XML_FRAGMENT)

# match_replace(RULES_EVDEV_LST, 'Romanian (WinKeys)', 'Romanian (WinKeys)', LST_FRAGMENT)
# match_replace(RULES_BASE_LST, 'Romanian (WinKeys)', 'Romanian (WinKeys)', LST_FRAGMENT)

# TODO: use regex here?
match_replace(SYMBOLS_RO, 'xkb_symbols "winkeys"', 'partial', SYMBOLS_RO_FRAGMENT)
