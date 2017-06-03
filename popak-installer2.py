import logging
import logging.config
import re
from shutil import copy2

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('popak-installer')

# constants
DIR_RULES = 'original/usr/share/X11/xkb/rules/'
DIR_SYMBOLS = 'original/usr/share/X11/xkb/symbols/'

RULES_BASE_XML = DIR_RULES + 'base.xml'
RULES_BASE_LST = DIR_RULES + 'base.lst'

RULES_EVDEV_XML = DIR_RULES + 'evdev.xml'
RULES_EVDEV_LST = DIR_RULES + 'evdev.lst'

SYMBOLS_RO = DIR_SYMBOLS + 'ro'

EXT_BACKUP = '.backup'


# backup first

def backup(file):
    file_backup = file + EXT_BACKUP
    logging.debug('creating backup for ' + file + ' -> ' + file_backup)
    # copy2(src,dst)
    copy2(file, file_backup)


# backup(RULES_BASE_XML)
# backup(RULES_BASE_LST)

# backup(RULES_EVDEV_XML)
# backup(RULES_EVDEV_LST)

# backup(SYMBOLS_RO)

f = open(RULES_EVDEV_XML, 'r')
# print (f)
xml = f.read()

# print (xml)

m = re.search('(?s)<variant>.+?Romanian\s+\(WinKeys\).+?</variant>', xml)

print(m.group(0))
