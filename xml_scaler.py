import os
import xml.etree.ElementTree as ET
import sys
import re

pattern = "-?\d+"
SCALE = 4


def scale_node_text(node):
    node.text = str(int(node.text) * SCALE)


def scaler(node):
    if re.match(pattern, node.text):
        scale_node_text(node)
    elif len(list(node)) != 0:
        for kid in node:
            scaler(kid)


def process_property(node):
    for item in node:
        if re.match(pattern, item.text):
            scale_node_text(item)


def process_sprites(node):
    for item in node.findall("Entry"):
        for kid in item.findall("Overwrite"):
            scaler(kid)


def process_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == "DefaultSpriteProperties":
            process_property(child)
        elif child.tag in ("SpriteTable", "AnimationTable", "NinePatchTable"):
            process_sprites(child)
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
        parsed_tree = process_xml(inputFilename)
        write_xml(parsed_tree, outputFilename)

