#!/usr/bin/env python3

import time
import random

WORDS_MAIN = ['mama', 'tato', 'Max']
WORDS_SUPPLEMENTAL = ['a', 'b', 'c', 'd', 'z']
WORDS_COUNT = 100

random.seed(time.time())
for i in range(WORDS_COUNT):
    if random.randrange(100) <10:
        list_for_next_word = WORDS_MAIN
    else:
        list_for_next_word = WORDS_SUPPLEMENTAL
    next_word = random.choice(list_for_next_word)
    print(next_word, end=' ')
