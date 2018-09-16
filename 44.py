"""Implementation of map() using comprehensions appropriately named fffmap(). Didn't see that coming, did ya?"""


def fffmap(input_list, key):
    """Insert a masturbation joke here"""
    return [key(x) for x in input_list]


print(fffmap(range(5), key=lambda a: a*a))
