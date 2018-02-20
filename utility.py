
import os

RESX = ".resx"
CSV = ".csv"

NAME = "name"

XML_DATA = "data"
XML_NAME = "name"
XML_VALUE = "value"

def prep_resx_name(directory, lang_code, tablename):
    return os.path.join(directory, lang_code, tablename + RESX)