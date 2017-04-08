import os
from xml.etree import ElementTree


def indent(elem, level = 0):
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


DIR_RULES   = 'installed/usr/share/X11/xkb/rules/'
DIR_SYMBOLS = 'installed/usr/share/X11/xkb/symbols/'

BASE_XML = DIR_RULES + 'base.xml'
BASE_LST = DIR_RULES + 'base.lst'

EVDEV_XML = DIR_RULES + 'evdev.xml'
EVDEV_LST = DIR_RULES + 'evdev.lst'

# print(os.listdir())

tree = ElementTree.parse(EVDEV_XML)
root = tree.getroot()

indent(root)

for element in root.findall("."):
    print(element.tag)

#for element in rădăcină.findall("./"):
#    #print('-----------------------------------------------------------------------------------')
#    #print(ElementTree.tostring(element, 'unicode'))
#    print(element.tag)

#print('--- models ------------------------------------------------------------------------')
#for model in rădăcină.findall("./modelList/model/configItem"):
#    print(model.find("name").text)
#    print('    ' + model.find("description").text)
#    print('    ' + model.find("vendor").text)

print('--- layouts -----------------------------------------------------------------------')
for layout in root.findall("./layoutList/layout/configItem"):
    print(layout.find("name").text)
    print('    ' + layout.find("shortDescription").text)
    print('    ' + layout.find("description").text)

#ElementTree.dump(rădăcină)

# inFile = open(EVDEV_XML, DOARCITIRE)
# conținut_xml = inFile.read()
# print(conținut_xml)
# for element in rădăcină.iter():
#     print(ET.tostring(element, 'unicode'))
