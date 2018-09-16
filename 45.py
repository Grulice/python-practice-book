"""Implementation of filter() using comprehensions appropriately named shmilter()"""


def shmilter(input_list, key):
    return [y for y in input_list if key(y)]


print(shmilter(range(5), key=lambda a: True if a % 2 == 0 else False))
