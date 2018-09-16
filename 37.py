import sys

try:
    f = open(sys.argv[1], 'r')
except FileNotFoundError as err:
    print(err)

for elem in f.readlines():
    print(elem[::-1])

f.close()
