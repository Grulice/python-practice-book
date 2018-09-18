"""Problem 57: Write a function invertdict to interchange keys and values in a dictionary.
For simplicity, assume that all values are unique."""


def invertdict(input_dict):
    return {v: k for (k, v) in input_dict.items()}


print(invertdict({'x': 1, 'y': 2, 'z': 3}))
