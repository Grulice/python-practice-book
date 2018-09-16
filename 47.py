"""Problem 47: Write a function enumerate that takes a list and returns a list of tuples containing
(index,item) for each item in the list."""


def memenumerate(input_list):
    return [(x, y) for (x, y) in zip(range(len(input_list)), input_list)]


print(memenumerate(["a", "b", "c"]))