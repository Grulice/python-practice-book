"""Problem 60: Write a program to list all the files in the given directory along with their length and last
modification time. The output should contain one line for each file containing filename, length and modification date
separated by tabs. Hint: see help for os.stat."""

import os
import sys


# if no argument is provided - DIR is set to current directory
try:
    DIR = sys.argv[1]
except IndexError:
    DIR = os.curdir

curr_dir_files = next(os.walk(DIR))[2]

for file in sorted(curr_dir_files):
    absolute_path = os.path.abspath(file)
    print("{0}  {1}  {2}".format(file, os.stat(absolute_path)[6], os.stat(absolute_path)[8]))
    #                                  st_size                            st_mtime
