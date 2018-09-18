"""Problem 59: Write a program extcount.py to count number of files for each extension in the given directory.
The program should take a directory name as argument and print count and extension for each available file extension."""

import os
import sys


# if no argument is provided - DIR is set to current directory
try:
    DIR = sys.argv[1]
except IndexError:
    DIR = os.curdir


def count_extensions(input_directory='.'):
    """Returns dict with file extensions as keys and the number of their occurrences as values"""
    extensionCountDict = {}
    for filename in next(os.walk(input_directory))[2]:
        fileExtension = filename.split('.')[1]
        if extensionCountDict.get(fileExtension):  # check if the key exists, create it if it doesn't
            extensionCountDict[fileExtension] += 1  # increment the counter of instances of extension
        else:
            extensionCountDict.setdefault(fileExtension, 1)  # if the key doesn't exist - create and initialize
    return extensionCountDict


for item in count_extensions(DIR).items():
    print("{0} - {1}".format(item[0], item[1]))

