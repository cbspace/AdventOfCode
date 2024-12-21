#!/usr/bin/env python
# Advent Of Code 2024 Day 9 by Craig Brennan
# https://adventofcode.com/2024/day/9

data = open('input/day9_input.txt').read().strip()
buffer = []

number = 0
for i,block_val in enumerate(data):
    is_free = i%2
    for x in range(int(block_val)):
        if is_free:
            buffer.append(-1)
        else:
            buffer.append(str(number))
    if not is_free: number += 1

start_pointer = 0
end_pointer = len(buffer) - 1

def get_blocks(buffer,start_pointer, end_pointer):
    at_end = False
    
    if start_pointer <= end_pointer:
        start_block = buffer[start_pointer]
        start_pointer += 1
    else:
        return True, start_pointer, end_pointer, ''

    while start_block != -1:
        if start_pointer <= end_pointer:
            start_block = buffer[start_pointer]
            start_pointer += 1
        else:
            at_end = True
            break

    if start_pointer <= end_pointer:
        end_block = buffer[end_pointer]
        end_pointer -= 1
    else:
        return True, start_pointer, end_pointer, ''

    while end_block == -1:
        if start_pointer <= end_pointer:
            end_block = buffer[end_pointer]
            end_pointer -= 1
        else:
            at_end = True
            break

    return at_end, start_pointer, end_pointer, end_block

at_end, start_pointer, end_pointer, end_block = get_blocks(buffer, start_pointer, end_pointer)
while not at_end:
    buffer[start_pointer-1] = end_block
    buffer[end_pointer+1] = -1
    at_end, start_pointer, end_pointer, end_block = get_blocks(buffer, start_pointer, end_pointer)

part1_sum = 0
for i,block in enumerate(buffer):
    if block != -1:
        part1_sum += i * int(block)

print(f'Part 1: {part1_sum}')