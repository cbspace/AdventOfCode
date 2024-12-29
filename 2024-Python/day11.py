#!/usr/bin/env python
# Advent Of Code 2024 Day 11 by Craig Brennan
# https://adventofcode.com/2024/day/11

# Using a recursive function along with memoization
def process_stone(stone, blinks, blink_limit, memo):
    if blinks < blink_limit:
        if (stone, blinks) in memo:
            return memo[(stone, blinks)]
        if stone == 0:
            count = process_stone(1, blinks + 1, blink_limit, memo)
        else:
            stone_str = str(stone)
            stone_strlen = len(stone_str)
            if stone_strlen % 2 == 0:          
                count = (process_stone(int(stone_str[0:stone_strlen//2]), blinks + 1, blink_limit, memo)
                        + process_stone(int(stone_str[stone_strlen//2:]), blinks + 1, blink_limit, memo))
            else:
                count = process_stone(stone*2024, blinks + 1, blink_limit, memo)
        memo[(stone, blinks)] = count
        return count
    else:
        return 1

file = open('input/day11_input.txt')
stones = [int(x) for x in file.read().split()]
part1_count, part2_count = 0, 0

for stone in stones:
    part1_count += process_stone(stone, 0, 25, {})
    part2_count += process_stone(stone, 0, 75, {})

print(f'Part 1: {part1_count}')
print(f'Part 2: {part2_count}')
