#!/usr/bin/python3

import sys

infile = open("input/day3_input.txt","r")
sch = []
parts_sum = 0

for l in infile:
    sch.append(l.strip())

infile.close()

y_max = len(sch) - 1
x_max = len(sch[0]) - 1

def symbol_adjacent(y, x):
    symbol_found = False
    adj_squares = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

    for sq in adj_squares:
        y_val = y + sq[0]
        x_val = x + sq[1]
        if y_val >= 0 and x_val >= 0 and y_val < y_max and x_val < x_max:
            symbol_found = not(sch[y_val][x_val].isdigit() or sch[y_val][x_val]==".") or symbol_found

    return symbol_found

y = 0
number_str = ""
symbol_found = False

for line in sch:
    if len(number_str) > 0:
        if symbol_found:
            parts_sum += int(number_str)
            symbol_found = False
        number_str = ""

    for x, c in enumerate(line):
        if c.isdigit():
            number_str += c
            symbol_found = symbol_adjacent(y,x) or symbol_found
        else:
            if len(number_str) > 0:
                if symbol_found:
                    parts_sum += int(number_str)
                    symbol_found = False
                number_str = ""

    y += 1

print("Part 1", parts_sum)