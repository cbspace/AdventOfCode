#!/usr/bin/env python
# Advent Of Code 2024 Day 9 by Craig Brennan
# https://adventofcode.com/2024/day/9

def create_buffer(data):
    buffer = []
    number = 0
    for i,block_val in enumerate(data):
        is_free = i%2
        for x in range(int(block_val)):
            if is_free:
                buffer.append(-1)
            else:
                buffer.append(number)
        if not is_free: number += 1
    return buffer

# Find contiguous blocks of length space starting from start_buffer
def find_space(buffer, start_pointer, end_pointer, length=1):
    counter = 0
    
    while start_pointer <= end_pointer:
        if buffer[start_pointer] == -1:
            counter += 1
            if counter == length:
                return start_pointer - length + 1
        else: 
            counter = 0
        start_pointer += 1

    return -1

def find_end_blocks(buffer, start_pointer, end_pointer, single=True):
    start_number = buffer[end_pointer]
    counter = 0

    while start_number == -1:
        end_pointer -= 1 
        start_number = buffer[end_pointer]

    if single:
        return end_pointer, 1

    while buffer[end_pointer] == start_number:
        counter += 1
        end_pointer -= 1
    
    return end_pointer + 1, counter

data = open('input/day9_input.txt').read().strip()

# Part 1
buffer = create_buffer(data)
start_pointer = 0
end_pointer = len(buffer) - 1

end_pointer, length = find_end_blocks(buffer, start_pointer, end_pointer)
start_pointer = find_space(buffer, start_pointer, end_pointer)
while start_pointer > -1 and end_pointer > -1:
    buffer[start_pointer] = buffer[end_pointer]
    buffer[end_pointer] = -1
    end_pointer, length = find_end_blocks(buffer, start_pointer, end_pointer-1)
    start_pointer = find_space(buffer, start_pointer, end_pointer-1)

part1_sum = 0
for i,x in enumerate(buffer):
    if x != -1:
        part1_sum += i * x

# Part 2
buffer = create_buffer(data)
start_pointer = 0
end_pointer = len(buffer) - 1

end_pointer, length = find_end_blocks(buffer, 0, end_pointer, single=False)
start_pointer = find_space(buffer, start_pointer, end_pointer, length)
at = end_pointer

while not at < 0:
    if start_pointer > -1:
        buffer[start_pointer:start_pointer+length] = buffer[end_pointer:end_pointer+length]
        buffer[end_pointer:end_pointer+length] = [-1] * length

    end_pointer, new_length = find_end_blocks(buffer, 0, end_pointer-1, single=False)
    start_pointer = find_space(buffer, 0, end_pointer-1, new_length)
    length = new_length
    at = end_pointer

part2_sum = 0
for i,x in enumerate(buffer):
    if x != -1:
        part2_sum += i * x

print(f'Part 1: {part1_sum}')
print(f'Part 2: {part2_sum}')