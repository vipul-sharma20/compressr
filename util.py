"""
Utility functions for filtering content
"""
from nltk import tokenize
from nltk.tokenize import word_tokenize
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG, LENGTH, REDUCED_LENGTH


def getWords(sentence):
    """
    Extracts words/tokens from a sentence
    :param sentence: (str) sentence
    :returns words_dict: (dict) dictionary of words
    :returns words: (list) word list
    """
    words = word_tokenize(sentence)
    words_dict = dict()
    words_dict[LENGTH] = len(sentence)
    words_dict[REDUCED_LENGTH] = words_dict[LENGTH]
    for word in words:
        words_dict[word] = {}
        words_dict[word][SUFFIX_FLAG] = False
        words_dict[word][PREFIX_FLAG] = False
        words_dict[word][REDUCED] = word
    return words_dict, words
