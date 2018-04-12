import os
import xml.etree.ElementTree as ET
import sys
import re

pattern = "\d+"
SCALE = 4



def parse_xml(filename):
    pass
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == "DefaultSpriteProperties":
            for item in child:
                if re.match(pattern, item.text):
                    item.text = item.text * SCALE
        elif child.tag in ("SpriteTable", "AnimationTable", "NinePatchTable"):
            for item in child:
                if item.tag == "Overwrite":





if len(sys.argv) != 2:
    print "Not enough argument added"
else:
    inputFilename = sys.argv[1]
    if not os.path.isfile(inputFilename):
        print "The added parameter is a directory give a file"
    else:
        outputFilename = inputFilename.result
        parse_xml(inputFilename)


