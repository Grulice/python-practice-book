import sys

try:
    f = open(sys.argv[1], 'r')
except FileNotFoundError as err:
    print(err)

lines = f.readlines()
first_ten = lines[:10]
last_ten = lines[-10:]
print(first_ten, last_ten)

f.close()
