"""Problem 53: Improve the above program to print the words in the descending order of the number of occurrences."""

import sys
from string import punctuation

#constants

FILE_PATH = "Dovlatov.txt"

def word_frequency(words):
    """Returns freq of each word given a list of words.
        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    freq = {}
    for w in words:
        cur_word = w.lower().strip(punctuation)
        freq[cur_word] = freq.get(cur_word, 0) + 1
    return freq


def read_words(filename):
    return open(filename).read().split()


frequency = word_frequency(read_words(FILE_PATH))
frequencyPairList = zip(frequency.keys(), frequency.values())
rank = 1

rankedFile = open(FILE_PATH.split('.')[0] + "_RANKED.txt", 'w')


for elem in sorted(frequencyPairList, key=lambda val: val[1], reverse=True):
    print("{0} -- {1} : {2} ".format(rank, elem[0], elem[1]))
    rankedFile.write("{0} -- {1} : {2} \n".format(rank, elem[0], elem[1]))
    rank += 1

rankedFile.close()