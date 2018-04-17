import os
import xml.etree.ElementTree as ET
import sys
import re

pattern = "\d+"
SCALE = 4


def all_scaler(node):
    if re.match(pattern, node.text):
        node.text = str(int(node.text) * SCALE)
    elif len(list(node)) != 0:
        for kid in node:
            all_scaler(kid)


def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == "DefaultSpriteProperties":
            for item in child:
                if re.match(pattern, item.text):
                    item.text = str(int(item.text) * SCALE)
        elif child.tag in ("SpriteTable", "AnimationTable", "NinePatchTable"):
            for item in child:
                if item.tag == "Overwrite":
                    all_scaler(item)
    return tree

def write_xml(tree, output):
    with open(output, "w") as xmlFile:
        xmlFile.write('<?xml version="1.0" encoding="utf-8"?>\n')
        tree.write(xmlFile, encoding='utf-8')

if len(sys.argv) != 2:
    print "Not enough argument added"
else:
    inputFilename = sys.argv[1]
    if not os.path.isfile(inputFilename):
        print "The added parameter is a directory give a file"
    else:
        outputFilename = inputFilename + ".result"
        parsed_tree = parse_xml(inputFilename)
        write_xml(parsed_tree, outputFilename)

