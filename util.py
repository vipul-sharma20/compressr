"""
Utility functions for filtering content
"""
from nltk import tokenize
from nltk.tokenize import TweetTokenizer
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG, LENGTH, \
        REDUCED_LENGTH, VOWEL_FLAG, ITEMTYPE, HASHTAG, URL, DEFAULT

import re

def getWords(sentence):
    """
    Extracts words/tokens from a sentence
    :param sentence: (str) sentence
    :returns words_dict: (dict) dictionary of words
    :returns words: (list) word list
    """
    word_tokenize = TweetTokenizer()
    words = word_tokenize.tokenize(sentence)
    words_dict = dict()
    words_dict[LENGTH] = len(sentence)
    words_dict[REDUCED_LENGTH] = words_dict[LENGTH]
    for word in words:
        words_dict[word] = {}
        words_dict[word][SUFFIX_FLAG] = False
        words_dict[word][PREFIX_FLAG] = False
        words_dict[word][VOWEL_FLAG] = False
        words_dict[word][ITEMTYPE] = check_itemtype(word)
        words_dict[word][REDUCED] = word
    return words_dict, words

def check_itemtype(word):
    """
    Check itemtype (hashtags, urls, default)
    :param word: (str) word
    :returns itemtype
    """
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word)
    if word[0] == '#':
        return HASHTAG

    elif urls:
        return URL
    else:
        return DEFAULT

