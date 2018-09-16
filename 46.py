"""Write a function triplets that takes a number n as argument and returns a list of triplets such
that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a,
b, c) and (b, a, c) represent same triplet."""


def triplet(n):
    return [(x, y, n) for n in range(n) for x in range(1, n) for y in range(x, n) if x + y == n]


print(triplet(5))
