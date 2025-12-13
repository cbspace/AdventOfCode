#!/usr/bin/env python
# Advent Of Code 2025 Day 1 by Craig Brennan
# https://adventofcode.com/2025/day/1

with open('input/day01_input.txt') as f:
    lines = f.read().split('\n')[:-1]

zero_landed = 0
zero_passed_count = 0
dial_pos = 50

for line in lines:
    direction, amount = line[0], int(line[1:])
    zero_passed_count += abs(amount // 100)

    if direction == 'L':
        new_pos = (dial_pos - amount) % 100
        if new_pos >= dial_pos and dial_pos != 0 and new_pos != 0:
            zero_passed_count += 1
    elif direction == 'R':
        new_pos = (dial_pos + amount) % 100
        if new_pos <= dial_pos and dial_pos != 0 and new_pos != 0:
            zero_passed_count += 1

    dial_pos = new_pos
    if dial_pos == 0:
        zero_landed += 1

print(f'Part 1: {zero_landed}')
print(f'Part 2: {zero_landed + zero_passed_count}')