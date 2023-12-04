#!/usr/bin/python3

import sys

infile = open("input/day4_input.txt","r")
winning_sum = 0

for l in infile:
    line = l.strip()
    card_numbers = line.split(": ")[1].split(" | ")
    my_numbers = card_numbers[0].split()
    winning_numbers = card_numbers[1].split()

    matching = 0

    for m in my_numbers:
        for w in winning_numbers:
            if m == w:
                matching += 1

    score = 2**(matching-1) if matching > 0 else 0
    winning_sum += score

infile.close()

print("Part 1: ", winning_sum)