"""Problem 56: Write a function valuesort to sort values of a dictionary based on the key."""

import sys
from string import punctuation


def valuesort(input_dict):
    return [v[1] for v in sorted(input_dict.items(), key=lambda x: x[0])]


print(valuesort({'x': 1, 'y': 2, 'a': 3}))
