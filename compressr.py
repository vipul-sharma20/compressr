# -*- coding: utf-8 -*-

import util
from slang import *
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG, LENGTH


def reduce_suffix(words_dict, words, limit):
    """
    Reduce suffix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words (list) word list
    :returns: reduced words dictionary
    """
    text_length = words_dict[LENGTH]
    for word in words:
        if text_length <= limit:
            return words_dict
        if not words_dict[word][SUFFIX_FLAG]:
            word_length = len(word)
            if word_length > 3:
                suffix_3 = word[-3:]
                suffix_4 = word[-4:]
                if suffix_3 in suffix_slang_3:
                    words_dict[word][REDUCED] = word[:-3] + \
                            suffix_slang_3[suffix_3]
                    text_length -= len(suffix_slang_3[suffix_3])
                if suffix_4 in suffix_slang_4:
                    words_dict[word][REDUCED] = word[:-4] + \
                            suffix_slang_4[suffix_4]
                    text_length -= len(suffix_slang_4[suffix_4])

        words_dict[word][SUFFIX_FLAG] = True
    return words_dict


def reduce_prefix(words_dict, words, limit):
    """
    Redue prefix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :returns: reduced words dictionary
    """
    text_length = words_dict[LENGTH]
    for word in words:
        if text_length <= limit:
            return words_dict
        if not words_dict[word][PREFIX_FLAG]:
            word_length = len(word)
            if word_length > 3:
                prefix_3 = word[:3]
                prefix_4 = word[:4]
                if prefix_3 in prefix_slang_3:
                    words_dict[word][REDUCED] = prefix_slang_3[prefix_3] + \
                            word[3:]
                    text_length -= len(prefix_slang_3[prefix_3])
                if prefix_4 in prefix_slang_4:
                    words_dict[word][REDUCED] = prefix_slang_4[prefix_4] + \
                            word[4:]
                    text_length -= len(prefix_slang_4[prefix_4])

        words_dict[word][PREFIX_FLAG] = True
    return words_dict


def get_text():
    """
    Driver function; Execution starts here
    """
    text = raw_input('')
    limit = input()
    words_dict, words = util.getWords(text)
    words_sorted = sorted(words)
    words_dict = reduce_suffix(words_dict, words_sorted, limit)
    words_dict = reduce_prefix(words_dict, words_sorted, limit)
    for word in words:
        print words_dict[word][REDUCED],

get_text()
