"""Problem 55: Write a program to find anagrams in a given list of words.
Two words are called anagrams if one word can be formed by rearranging letters of another.
For example ‘eat’, ‘ate’ and ‘tea’ are anagrams."""

import sys
from string import punctuation


def anagrams(input_list):

    anagram_dict = {}  # keys-sorted strings of letters that make up the word; values-words containing letters from key
    for word in input_list:
        letters_sorted = ''.join(sorted(word))  # sorted() returns list of chars; ''.join() converts list back to str
        anagram_dict.setdefault(letters_sorted, [])  # create the key if it's not found
        anagram_dict[letters_sorted].append(word)  # append the word to appropriate list in the dict

    return [v for v in anagram_dict.values()]


print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node', 'latte', 'tatle']))
