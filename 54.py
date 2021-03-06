"""Problem 54: Write a program to count frequency of characters in a given file. Can you use character frequency
to tell whether the given file is a Python program file, C program file or a text file?"""

import sys
from string import punctuation
from string import ascii_lowercase

#constants

FILE_PATH = "Dovlatov.txt"


def char_frequency(words):
    """Returns freq of each word given a list of words.
        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    freq = {}
    for word in words:
        for character in word.lower():
            if character in ascii_lowercase:
                freq[character] = freq.get(character, 0) + 1
    return freq


def read_words(filename):
    return open(filename).read().split()


frequency = char_frequency(read_words(FILE_PATH))
frequencyPairList = zip(frequency.keys(), frequency.values())
rank = 1

rankedFile = open(FILE_PATH.split('.')[0] + "_RANKED.txt", 'w')


for elem in sorted(frequencyPairList, key=lambda val: val[1], reverse=True):
    print("{0} -- {1} : {2} ".format(rank, elem[0], elem[1]))
    rankedFile.write("{0} -- {1} : {2} \n".format(rank, elem[0], elem[1]))
    rank += 1

rankedFile.close()