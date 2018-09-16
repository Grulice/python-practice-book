"""Problem 48: Write a function array to create an 2-dimensional array. The function should take both dimensions
as arguments. Value of each element can be initialized to None:"""


def array2d(x, y):
    return [[None]*y]*x


print(array2d(2, 3))