"""Problem 61: Write a program to print directory tree.
The program should take path of a directory as argument and print all the files in it recursively as a tree."""

import os
import sys


# if no argument is provided - DIR is set to current directory
try:
    DIR = sys.argv[1]
except IndexError:
    DIR = os.curdir

sign = lambda x: x and (1, -1)[x < 0]
# for some reason the math module does not have a sign() function, so we make one, just like ma' used to


for layer in os.walk(DIR):  # see docstrings of os.walk() to understand what it returns
    padding = '|  ' * (len(layer[0].split('/')) - 1)
    # layer[0] is the relative path to current parent folder.
    # The list you get when you split it by '/' is the list of all parent folders (up to the start folder),
    # plus the current folder. The length of this list tells us how many parent folders the current folder has,
    # but we have to subtract 1 to account for the current folder. This allows us to prepare the padding string
    # for the files that are going to follow in the for loop below. The padding string allows the files to be
    # displayed at the correct depth

    folder_indicator = '|==' * sign(len(layer[0].split('/')) - 1)
    # |== is the symbol that signifies a folder in the tree.
    # sign(len(layer[0].split('/')) - 1) will be equal to 0 only at the first layer, afterwards it will always be 1
    # this is done so that the root folder symbol '.' at layer 0 is shown properly,
    # without a preceding folder indicator '|=='. This is a side effect of how we calculate the current depth.
    # This solution feels like a bit of a crutch. It would be better to think of a better solution.
    # TODO: Find a better solution for removing the folder indicator for the root folder

    print(padding[:-3] + folder_indicator + layer[0].split('/')[-1])
    # Print the name of the current folder. We swap the last padding symbol '|  ' for a folder indicator '|=='.
    for file in layer[2]:
        print("{0}|--{1}".format(padding, file))
        # Print the padding, the file indicator |-- and the file name
        # layer[2] is the list of file names in the current folder

