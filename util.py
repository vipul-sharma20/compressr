"""
Utility functions for filtering content
"""
from nltk import tokenize
from nltk.tokenize import word_tokenize


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
        words_dict[word]['lower'] = None
        words_dict[word]['upper'] = None
        words_dict[word]['flag'] = False
        words_dict[word]['reduced'] = ''
    return words_dict
