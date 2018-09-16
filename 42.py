"""Center align lines of a file"""

import sys
from copy import copy

#input constants
file_path = "centeralign.txt"
max_line_width = 30

#open the file
try:
    f = open(file_path, 'r')
except FileNotFoundError as err:
    print(err)

#constants
file_lines = f.readlines()
center_index = len(
    max(file_lines, key=lambda s: len(s))
)/2  # find the index of the character in the middle of the longest line


for line in file_lines:
    left_padding_length = round(center_index - len(line)/2)
    left_padding = ' ' * left_padding_length
    print(left_padding, line)

#close the file
f.close()
