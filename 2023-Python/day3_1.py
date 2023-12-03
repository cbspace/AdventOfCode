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

# TODO: Fix this mess
def symbol_adjacent(y, x):
    left = not(sch[y][x-1].isdigit() or sch[y][x-1]==".") if x > 0 else False
    right = not(sch[y][x+1].isdigit() or sch[y][x+1]==".") if x < x_max else False
    up = not(sch[y-1][x].isdigit() or sch[y-1][x]==".") if y > 0 else False
    down = not(sch[y+1][x].isdigit() or sch[y+1][x]==".") if y < y_max else False

    left_up = not(sch[y-1][x-1].isdigit() or sch[y-1][x-1]==".") if x > 0 and y > 0 else False
    right_up = not(sch[y-1][x+1].isdigit() or sch[y-1][x+1]==".") if x < x_max and y > 0 else False
    left_down = not(sch[y+1][x-1].isdigit() or sch[y+1][x-1]==".") if y < y_max and x > 0 else False
    right_down = not(sch[y+1][x+1].isdigit() or sch[y+1][x+1]==".") if y < y_max and x < x_max else False

    return left or right or up or down or left_up or right_up or left_down or right_down

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