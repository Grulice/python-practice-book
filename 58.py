"""Problem 58: Write a program to list all files in the given directory."""

import os
import sys


# change this to be the directory you want
DIR = sys.argv[1]

print(next(os.walk(DIR))[2])

#os.walk() is a generator, so we need to use next() to get only the first value
