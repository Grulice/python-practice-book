# Problem 69: Write a program mydoc.py to implement the functionality of pydoc. The program should take
# the module name as argument and print documentation for the module and each of the functions defined in that
# module.
# Hints:
# • The dir function to get all entries of a module
# • The inspect.isfunction function can be used to test if given object is a function
# • x.__doc__ gives the docstring for x.
# • The __import__ function can be used to import a module by name

import sys
import zipfile

ARCHIVE_NAME = sys.argv[1]
FILES = sys.argv[2:]

z = zipfile.ZipFile("./assets/{0}".format(ARCHIVE_NAME), 'w')  # open the archive in write mode

for FILE in FILES:
    z.write(FILE)  # write files to the archive
z.close()  # close the archive when done
