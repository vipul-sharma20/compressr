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
    return words
