import logging
import logging.config
from shutil import copy2
from xml.etree import ElementTree

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


def indent(elem, level=0):
    i = "\n" + level * "  "
    j = "\n" + (level - 1) * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


# print(os.listdir())

tree = ElementTree.parse(RULES_EVDEV_XML)
root = tree.getroot()

indent(root)

for element in root.findall("."):
    print(element.tag)

# for element in rădăcină.findall("./"):
#    #print('-----------------------------------------------------------------------------------')
#    #print(ElementTree.tostring(element, 'unicode'))
#    print(element.tag)

# print('--- models ------------------------------------------------------------------------')
# for model in rădăcină.findall("./modelList/model/configItem"):
#    print(model.find("name").text)
#    print('    ' + model.find("description").text)
#    print('    ' + model.find("vendor").text)

print('--- layouts -----------------------------------------------------------------------')


def print_layout(layout):
    print(layout.find("configItem/name").text)
    print('    ' + layout.find("configItem/shortDescription").text)
    print('    ' + layout.find("configItem/description").text)
    for variant in layout.findall("./variantList/variant/configItem"):
        print('        ' + variant.find("name").text)
        print('        ' + variant.find("description").text)


layout_ro = root.find("./layoutList/layout/configItem[name='ro']/..")
print(ElementTree.tostring(layout_ro, 'unicode'))
print_layout(layout_ro)

# for layout in root.findall("./layoutList/layout"):
#    print_layout(layout)


# ElementTree.dump(rădăcină)

# inFile = open(RULES_EVDEV_XML, DOARCITIRE)
# conținut_xml = inFile.read()
# print(conținut_xml)
# for element in rădăcină.iter():
#     print(ET.tostring(element, 'unicode'))
