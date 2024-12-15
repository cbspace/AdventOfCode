#!/usr/bin/env python
# Advent Of Code 2024 Day 7 by Craig Brennan
# https://adventofcode.com/2024/day/7

import numpy as np

def get_result(numbers, operators):
    calculated_result = numbers[0]

    for i in range(len(numbers) - 1):
        match operators[i]:
            case '0':
                calculated_result += numbers[i+1]
            case '1':
                calculated_result *= numbers[i+1]
            case '2':
                calculated_result = int(str(calculated_result) + str(numbers[i+1]))
    return calculated_result

part1_total, part2_total = 0, 0
file = open('input/day7_input.txt')
equations = []

for line in file.readlines():
    result = line.split(':')[0]
    numbers = line.split(':')[1].split()
    equations.append([int(result), [int(n) for n in numbers]])

for eq in equations:
    result_match = False
    digits = len(eq[1]) - 1
    for i in range(2**digits):
        binary = format(i, f'0{digits}b')
        calculated_result = get_result(eq[1], binary)
        if(calculated_result == eq[0]):
            result_match = True
            part1_total += calculated_result
            part2_total += calculated_result
            break
    if not result_match:
        for i in range(3**digits):
            base3 = np.base_repr(i,3).zfill(digits)
            calculated_result = get_result(eq[1], base3)
            if(calculated_result == eq[0]):
                part2_total += calculated_result
                break

print(f'Part 1: {part1_total}')
print(f'Part 2: {part2_total}')