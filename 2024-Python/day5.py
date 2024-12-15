#!/usr/bin/env python
# Advent Of Code 2024 Day 5 by Craig Brennan
# https://adventofcode.com/2024/day/5

file = open('input/day5_input.txt')

number_list = []
run_list = []
reached_blank = False

part1_total, part2_total = 0, 0

def check_list(number_list, run):
    success = True
    error_a, error_b = 0, 0
    for a,b in number_list:
        if a in run and b in run:
            a_index, b_index = run.index(a), run.index(b)
            if not(a_index < b_index):
                success = False
                error_a, error_b = a_index, b_index
                break
    return success, error_a, error_b

for line in file.readlines():
    line = line.strip()

    if not len(line):
        reached_blank = True
        continue

    if not reached_blank:
        number_list.append([int(line[:2]), int(line[3:])])
    else:
        run_list.append([int(x) for x in line.split(',')])

for update in run_list:
    update_ok, error_a, error_b = check_list(number_list, update)

    if update_ok:
        part1_total += update[len(update)//2]
    else:
        while not update_ok:
            temp = update[error_a]
            update[error_a] = update[error_b]
            update[error_b] = temp
            update_ok, error_a, error_b = check_list(number_list, update)
        part2_total += update[len(update)//2]

print(f'Part 1: {part1_total}')
print(f'Part 2: {part2_total}')