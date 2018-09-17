"""Problem 55: Write a program to find anagrams in a given list of words.
Two words are called anagrams if one word can be formed by rearranging letters of another.
For example ‘eat’, ‘ate’ and ‘tea’ are anagrams."""

import sys
from string import punctuation


def anagrams(input_list):
    result = []
    anagramDict = {}
    for word in input_list:
        for char in word:
