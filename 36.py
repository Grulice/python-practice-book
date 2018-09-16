import sys

try:
    f = open(sys.argv[1], 'r')
except FileNotFoundError as err:
    print(err)

for elem in reversed(f.readlines()):
    print(elem)

f.close()
