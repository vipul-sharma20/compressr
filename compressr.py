# -*- coding: utf-8 -*-

import util
import bitly_api
from slang import *
from constants import REDUCED, SUFFIX_FLAG, PREFIX_FLAG, VOWEL_FLAG, LENGTH, \
        REDUCED_LENGTH, VOWELS, ITEMTYPE, DEFAULT, ACCESS_TOKEN, URL


def reduce_suffix(words_dict, words, limit):
    """
    Reduce suffix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :param limit: (int) character limit
    :returns: reduced words dictionary
    """
    for word in words:
        if words_dict[REDUCED_LENGTH] <= limit:
            return words_dict
        if not words_dict[word][SUFFIX_FLAG] and \
                words_dict[word][ITEMTYPE] == DEFAULT:
            word_length = len(word)
            if word_length > 3:
                suffix_3 = word[-3:]
                suffix_4 = word[-4:]
                if suffix_3 in suffix_slang_3:
                    words_dict[word][REDUCED] = word[:-3] + \
                            suffix_slang_3[suffix_3]
                    words_dict[REDUCED_LENGTH] -= len(suffix_slang_3[suffix_3])

                    words_dict[word][SUFFIX_FLAG] = True

                if suffix_4 in suffix_slang_4:
                    words_dict[word][REDUCED] = word[:-4] + \
                            suffix_slang_4[suffix_4]
                    words_dict[REDUCED_LENGTH] -= len(suffix_slang_4[suffix_4])

                    words_dict[word][SUFFIX_FLAG] = True
        else:
            if words_dict[word][ITEMTYPE] == URL:
                url = shorten_url(word)
                words_dict[word][REDUCED] = url
                words_dict[REDUCED_LENGTH] -= (len(word)-len(url))

    return words_dict


def reduce_prefix(words_dict, words, limit):
    """
    Redue prefix from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :param limit: (int) character limit
    :returns: reduced words dictionary
    """
    for word in words:
        if words_dict[REDUCED_LENGTH] <= limit:
            return words_dict
        if not words_dict[word][PREFIX_FLAG] and words_dict[word][ITEMTYPE] == DEFAULT:
            word_length = len(word)
            if word_length > 3:
                prefix_3 = word[:3]
                prefix_4 = word[:4]
                if prefix_3 in prefix_slang_3:
                    words_dict[word][REDUCED] = prefix_slang_3[prefix_3] + \
                            word[3:]
                    words_dict[REDUCED_LENGTH] -= len(prefix_slang_3[prefix_3])

                    words_dict[word][PREFIX_FLAG] = True
                if prefix_4 in prefix_slang_4:
                    words_dict[word][REDUCED] = prefix_slang_4[prefix_4] + \
                            word[4:]
                    words_dict[REDUCED_LENGTH] -= len(prefix_slang_4[prefix_4])

                    words_dict[word][PREFIX_FLAG] = True
        else:
            if words_dict[word][ITEMTYPE] == URL:
                url = shorten_url(word)
                words_dict[word][REDUCED] = url
                words_dict[REDUCED_LENGTH] -= (len(word)-len(url))

    return words_dict


def reduce_vowels(words_dict, words, limit):
    """
    Reduce vowels from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :param limit: (int) character limit
    :returns: reduced words dictionary
    """
    for word in words:
        if words_dict[word][ITEMTYPE] == DEFAULT and len(word) > 3:
            temp_reduced = words_dict[word][REDUCED][1:-1]
            for v in VOWELS:

                # :FIX: This is a bad work around.
                temp = temp_reduced.replace(v, '')
                words_dict[REDUCED_LENGTH] -= abs(len(temp_reduced) - len(temp))
                temp_reduced = temp
                words_dict[word][REDUCED] = words_dict[word][REDUCED][0] + \
                        temp_reduced + words_dict[word][REDUCED][-1]

                if words_dict[REDUCED_LENGTH] <= limit:
                    return words_dict
        words_dict[word][VOWEL_FLAG] = True
    return words_dict


def reduce_general_slang(words_dict, words, limit):
    """
    Reduce general slang from words
    :param words_dict: (dict) key-value pair of words from text
    :param words: (list) word list
    :param limit: (int) character limit
    :returns: reduced words dictionary
    """
    for word in words:
        if general_slang.get(word):
            words_dict[word][REDUCED] = general_slang[word]
            words_dict[REDUCED_LENGTH] -= len(general_slang[word])
            words_dict[word][PREFIX_FLAG] = True
            words_dict[word][SUFFIX_FLAG] = True
            words_dict[word][VOWEL_FLAG] = True
    return words_dict


def shorten_url(url):
    """
    Shorten URLs using Bitly
    :param url: (str) URL
    :returns: shortened URL
    """
    bitly_con = bitly_api.Connection(access_token=ACCESS_TOKEN)
    return bitly_con.shorten(url)[URL]


def get_text():
    """
    Driver function; Execution starts here
    """
    text = raw_input('TEXT: ')
    limit = input('LIMIT: ')
    words_dict, words = util.getWords(text)
    words_sorted = sorted(words, key=len)
    words_dict = reduce_general_slang(words_dict, words_sorted, limit)
    words_dict = reduce_suffix(words_dict, words_sorted, limit)
    words_dict = reduce_prefix(words_dict, words_sorted, limit)
    words_dict = reduce_vowels(words_dict, words_sorted, limit)

    for word in words:
        print words_dict[word][REDUCED],

get_text()
