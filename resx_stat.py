import sys
import os
import utility
import xml.etree.ElementTree as ET
import re

# resx_stat.py en -> String/en/*.resx
# resx_stat.py Item -> String/en/Item.resx

directory = "Strings"
lang_code = "en"


def create_stat(filename, table):
    tree = ET.parse(filename)
    root = tree.getroot()
    all_words = set()
    key_count = 0
    word_count = 0
    max_character_count = 0
    for data in root.findall(utility.XML_DATA):
        value = data.find(utility.XML_VALUE)
        value_text = str(value.text.encode(encoding="utf-8", errors="ignore")).lower()
        pattern = "[^a-zA-Z\s]+"
        value_text = re.sub(pattern, "", value_text)
        key_count += 1
        #words = value_text.split(" ")
        words = [x.strip() for x in value_text.split()]
        word_count += len(words)
        if max_character_count < len(value_text):
            max_character_count = len(value_text)
        all_words.update(words)
        all_unique_words.update(words)
    unique_count = len(all_words)
    table.append([key_count, word_count, max_character_count, unique_count])
#    print "keys: ", key_count
#    print "Words: ", word_count
#    print "Characters: ", max_character_count
#    print "Unique Words: ", unique_count


def create_global_stat(table):
    all_key_count = 0
    all_word_count = 0
    global_max_character_count = 0
    for item in table:
        all_key_count += item[0]
        all_word_count += item[1]
        if global_max_character_count < item[2]:
            global_max_character_count = item[2]
    global_unique_count = len(all_unique_words)
    print "global keys: ", all_key_count
    print "global words: ", all_word_count
    print "global max characters: ", global_max_character_count
    print "global unique Words: ", global_unique_count


if len(sys.argv) != 2:
    print "Not enough argument added"
else:
    table = []
    global all_unique_words
    all_unique_words = set()
    if os.path.isdir(sys.argv[1]):
        for i in xrange(len(os.listdir(sys.argv[1]))):
            filenames = os.path.join(directory, lang_code, os.listdir(sys.argv[1])[i])
            print filenames
            create_stat(filenames, table)
            print table[i]
        create_global_stat(table)
    else:
        filename = utility.prep_resx_name(directory, lang_code, sys.argv[1])
        create_stat(filename, table)
