import fileinput
import logging
import logging.config
from shutil import copy2

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('popak-installer')

# constants ------------------------------------------------------

DIR_RULES = 'original/usr/share/X11/xkb/rules/'
DIR_SYMBOLS = 'original/usr/share/X11/xkb/symbols/'

RULES_BASE_XML = DIR_RULES + 'base.xml'
RULES_BASE_LST = DIR_RULES + 'base.lst'

RULES_EVDEV_XML = DIR_RULES + 'evdev.xml'
RULES_EVDEV_LST = DIR_RULES + 'evdev.lst'

SYMBOLS_RO = DIR_SYMBOLS + 'ro'
EXT_BACKUP = '.backup'

EVDEV_XML_FRAGMENT = '''        <variant>
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


# methods --------------------------------------------------------

def backup(file):
    file_backup = file + EXT_BACKUP
    logging.debug('creating backup for ' + file + ' -> ' + file_backup)
    # copy2(src,dst)
    copy2(file, file_backup)


# installation logic ---------------------------------------------

# backup(RULES_BASE_XML)
# backup(RULES_BASE_LST)

# backup(RULES_EVDEV_XML)
# backup(RULES_EVDEV_LST)

# backup(SYMBOLS_RO)


evdev_xml_match = False
evdev_lst_match = False

base_xml_match = False
base_lst_match = False

with fileinput.FileInput(RULES_EVDEV_XML, inplace=True) as f:
    for line in f:
        if 'Romanian (WinKeys)' in line:
            evdev_xml_match = True
        if evdev_xml_match:
            if '</variant>' in line:
                line = line.replace(line, line + EVDEV_XML_FRAGMENT)
                logger.debug(line)
                print(line, end='')
                evdev_xml_match = False
            else:
                print(line, end='')
        else:
            print(line, end='')
