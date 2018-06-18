import os
import xml.etree.ElementTree as ET
import sys

SCALE = 4


def scale_node_text(node):
    node.text = str(int(node.text) * SCALE)


def process_property_list(node):
    node_text_list = node.text.split()
    scaled_node_text_list = []
    for item in node_text_list:
        scaled_node_text_list.append((str(int(item) * SCALE)))
    scaled_node_text = ' '.join(scaled_node_text_list)
    node.text = scaled_node_text


def process_property_glyph(node):
    pass


def process_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == "PlaceholderGlyph":
            process_property_list(child)
        elif child.text.isdigit():
            scale_node_text(child)
        elif child.tag == "Glyph":
            process_property_glyph(child)
        elif false:
            # todo attrib
            pass
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

