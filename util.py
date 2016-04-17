"""
Utility functions for filtering content
"""
from nltk import tokenize
from nltk.tokenize import word_tokenize
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG

def getWords(sentence):
    """
    Extracts words/tokens from a sentence
    :param sentence: (str) sentence
    :returns: list of tokens
    """
    words = word_tokenize(sentence)
    words_dict = dict()
    for word in words:
        words_dict[word] = {}
        words_dict[word][SUFFIX_FLAG] = False
        words_dict[word][PREFIX_FLAG] = False
        words_dict[word][REDUCED] = ''
    return words_dict, words
