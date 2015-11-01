# -*- coding: UTF-8 -*-


import xml.etree.ElementTree as etree

tree = etree.parse('../data/feed.xml')

root = tree.getroot()
print('root: ', root)

tag = root.tag
print('tag: ', tag)

attrib = root.attrib
print('attrib', attrib)

for child in root:
    print('child: ', child)