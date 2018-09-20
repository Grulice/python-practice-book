# Problem 68: Write a python program zip.py to create a zip file. The program should take name of zip file as first
# argument and files to add as rest of the arguments.

import sys
import zipfile

ARCHIVE_NAME = sys.argv[1]
FILES = sys.argv[2:]

z = zipfile.ZipFile("./assets/{0}".format(ARCHIVE_NAME), 'w')  # open the archive in write mode

for FILE in FILES:
    z.write(FILE)  # write files to the archive
z.close()  # close the archive when done
