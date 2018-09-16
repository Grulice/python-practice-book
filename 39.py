import sys

try:
    f = open(sys.argv[1], 'r')
except FileNotFoundError as err:
    print(err)

search_keyword = sys.argv[2]

for readline in f.readlines():
    if search_keyword in readline:
        print(readline)

f.close()
