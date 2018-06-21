import os
import xml.etree.ElementTree as ET
import sys

SCALE = 4


def scale_node_text(node):
    node.text = str(int(node.text) * SCALE)


def scale_node_attrib(node, attrib):
    node.attrib[attrib] = str(int(node.attrib[attrib]) * SCALE)


def generate_scaled_list(normal_list):
    for item in normal_list:
        yield str(int(item) * SCALE)


def process_property_list(node):
    node.text = ' '.join(generate_scaled_list(node.text.split()))
    #node.text = ' '.join(str(int(x) * SCALE) for x in node.text.split())
    #node.text = ' '.join(map(lambda x: str(int(x) * SCALE), node.text.split()))


def process_property_glyph(node):
    scale_node_attrib(node, 'advance')
    process_property_list(node)


def find_all_child(node):
    for child in node:
        if child.tag == "PlaceholderGlyph":
            process_property_list(child)
        elif child.text.isdigit():
            scale_node_text(child)
        elif child.tag == "Glyph":
            process_property_glyph(child)
        find_all_child(child)


def process_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    scale_node_attrib(root, 'height')
    find_all_child(root)
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

