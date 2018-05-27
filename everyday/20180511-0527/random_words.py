#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import os
from collections import Counter
from string import punctuation
from bisect import bisect

# load book's data.
def load_book(path='emma.txt'):
    # Load file
    words = []
    with open(path) as fin:
        for f in fin:
            words += f.split(' ')
    return words

def filter_punctual(words):
    clear_words = []
    for w in words:
        tmp_word = []
        for char in w.strip():
            if char in punctuation:
                pass
            else:
                tmp_word.append(char)
        clear_words.append(''.join(tmp_word).lower())
    return clear_words

def histogram(words=[]):
    new_words = [w for w in filter_punctual(words) if w]
    return dict(Counter(new_words))


def in_bisect(sorted_list, target_value):
    i = bisect(sorted_list, target_value)
    return i

path = '{0}'.format(os.path.abspath('emma.txt'))
his = histogram(load_book(path=path))
result_hist = sorted(his.items(), key=lambda x: x[1], reverse=True)
show = random.choice(result_hist)
index = in_bisect(sorted(result_hist), show)
# Output the index.
print(result_hist[index])
# Outout the result
