# -*- coding: utf-8 -*-

import util
from slang import *


def reduce_suffix(words):
    """
    Reduce suffix from words
    :param words (list) word list
    :returns: reduced word list
    """
    for word_index in range(len(words)):
        word = words[word_index]
        word_length = len(word)
        if word_length > 3:
            suffix_3 = word[-3:]
            suffix_4 = word[-4:]
            if suffix_3 in suffix_slang_3:
                words[word_index] = word[:-3] + suffix_slang_3[suffix_3]
            if suffix_4 in suffix_slang_4:
                words[word_index] = word[:-4] + suffix_slang_4[suffix_4]
    return words

def reduce_prefix(words):
    """
    Redue prefix from words
    :params: (list) word list
    :returns: reduced word list
    """
    for word_index in range(len(words)):
        word = words[word_index]
        word_length = len(word)
        if word_length > 3:
            prefix_3 = word[:3]
            prefix_4 = word[:4]
            if prefix_3 in prefix_slang_3:
                words[word_index] = prefix_slang_3[prefix_3] + word[3:]
            if prefix_4 in prefix_slang_4:
                words[word_index] = prefix_slang_4[prefix_4] + word[4:]
    return words

def get_text():
    text = raw_input('')
    words = util.getWords(text)
    words = reduce_suffix(words)
    words = reduce_prefix(words)
    print words

get_text()
