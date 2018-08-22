import sys
import os


EXTENSION = "jpg"


def do_command(file):
    print "do command" + file


if len(sys.argv) != 2:
    print "Not enough argument added"
else:
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print "Not a directory:", directory
    else:
        for root, dirs, filenames in os.walk(directory):
            for file in filenames:
                if file.endswith(EXTENSION):
                    full_path = os.path.join(root, file)
                    do_command(full_path)
