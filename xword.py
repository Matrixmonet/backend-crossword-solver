#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crossword Solver Program
Description: displays possible words to fit crossword puzzle location based on
dictionary of words
"""

__author__ = "Sarah Gale"

import re


def word_checker(in_word, words):
    """checks in_word against words list, to see if any match pattern"""
    """returns list as well as printing all matches"""
    regex = in_word.replace(' ', '\\w')
    word_list = []
    for word in words:
        if len(in_word) == len(word) and re.match(r'{0}'.format(regex), word):
            print(word)
            word_list.append(word)
    if not word_list:
        print("Sorry, No matches!")
    return word_list


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    # spaces represent unknown letters
    test_word = input(
        'Please enter a word to solve.\n\
        Use spaces to signify unknown letters: '
    ).lower()

    # test_word needs to be letters and spaces for unknown letters
    word_checker(test_word, words)


if __name__ == '__main__':
    main()
