#!/usr/bin/env python3

import time
import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--words-main', action="append", default=['mama', 'tato', 'Max'])
    parser.add_argument('--words-other', action="append", default=['a', 'b', 'c', 'd', 'z'])
    parser.add_argument('--words-count', type=int, default=100)
    parser.add_argument('--words-other-file')
    return parser.parse_args()


args = parse_args()
words_other = []
if args.words_other_file:
    with open(args.words_other_file, 'r') as data_file:
        words_other = [line.strip() for line in data_file]
else:
    words_other = args.words_other

random.seed(time.time())
for i in range(args.words_count):
    if random.randrange(100) < 10:
        list_for_next_word = args.words_main
    else:
        list_for_next_word = words_other
    next_word = random.choice(list_for_next_word)
    print(next_word, end=' ')
