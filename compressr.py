# -*- coding: utf-8 -*-

import util
from slang import *
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG


def reduce_suffix(words_dict, words):
    """
    Reduce suffix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words (list) word list
    :returns: reduced words dictionary
    """
    for word in words:
        if not words_dict[word][SUFFIX_FLAG]:
            word_length = len(word)
            if word_length > 3:
                suffix_3 = word[-3:]
                suffix_4 = word[-4:]
                if suffix_3 in suffix_slang_3:
                    words_dict[word][REDUCED] = word[:-3] + \
                            suffix_slang_3[suffix_3]
                elif suffix_4 in suffix_slang_4:
                    words_dict[word][REDUCED] = word[:-4] + \
                            suffix_slang_4[suffix_4]
                else:
                    if not words_dict[word][PREFIX_FLAG]:
                        words_dict[word][REDUCED] = word
            else:
                words_dict[word][REDUCED] = word

        words_dict[word][SUFFIX_FLAG] = True
    return words_dict


def reduce_prefix(words_dict, words):
    """
    Redue prefix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :returns: reduced words dictionary
    """
    for word in words:
        if not words_dict[word][PREFIX_FLAG]:
            word_length = len(word)
            if word_length > 3:
                prefix_3 = word[:3]
                prefix_4 = word[:4]
                if prefix_3 in prefix_slang_3:
                    words_dict[word][REDUCED] = prefix_slang_3[prefix_3] + \
                            word[3:]
                elif prefix_4 in prefix_slang_4:
                    words_dict[word][REDUCED] = prefix_slang_4[prefix_4] + \
                            word[4:]
                else:
                    if not words_dict[word][SUFFIX_FLAG]:
                        words_dict[word][REDUCED] = word
            else:
                words_dict[word][REDUCED] = word

        words_dict[word][PREFIX_FLAG] = True
    return words_dict


def get_text():
    """
    Driver function; Execution starts here
    """
    text = raw_input('')
    words_dict, words = util.getWords(text)
    words_dict = reduce_suffix(words_dict, words)
    words_dict = reduce_prefix(words_dict, words)
    for word in words:
        print words_dict[word][REDUCED],

get_text()
