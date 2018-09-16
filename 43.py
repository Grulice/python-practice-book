"""Implementation of zip() using comprehensions appropriately named zoop()"""

def zoop(list1, list2):
    """Evil zip() from the evil parallel universe"""
    return [(x, list2[list1.index(x)]) for x in list1]


print(zoop([1, 2, 3], ["a", "b", "c"]))