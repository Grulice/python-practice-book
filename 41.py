import sys
from copy import copy

#input constants
file_path = "she.txt"
max_line_width = 30

try:
    f = open(file_path, 'r')
except FileNotFoundError as err:
    print(err)




for readline in f.readlines():

    for word in readline.split():
        if readline.index(word) + len(word) > max_line_width:
            readline = readline[:readline.index(word)] + "\n" + readline[readline.index(word):]
            break
    print(readline)

f.close()
