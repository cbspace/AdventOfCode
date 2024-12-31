#!/usr/bin/env python
# Advent Of Code 2024 Day 13 by Craig Brennan
# https://adventofcode.com/2024/day/13

def solve(a0, a1, b0, b1, p0, p1):
    b = (p1 - a1 * (p0/a0)) / (b1 - a1 * (b0/a0))
    a = (p0 - b0*b) / a0

    delta_limit = 0.001
    delta_a = abs(a - round(a))
    delta_b = abs(b - round(b))

    if delta_a < delta_limit and delta_b < delta_limit:
        return round(a), round(b)
    else: 
        return 0,0

file = open('input/day13_input.txt')
games = file.read().split('\n\n')
total_part1, total_part2 = 0, 0

for game in games:
    game = game.strip()
    lines = game.split('\n')
    dataA = lines[0][10:].split(', ')
    dataB = lines[1][10:].split(', ')
    prize = lines[2][7:].split(', ')
    a0, a1 = int(dataA[0][2:]), int(dataA[1][2:])
    b0, b1 = int(dataB[0][2:]), int(dataB[1][2:])
    p0, p1 = int(prize[0][2:]), int(prize[1][2:])

    tokensA, tokensB = solve(a0, a1, b0, b1, p0, p1)
    total_part1 += 3*tokensA + tokensB

    tokensA, tokensB = solve(a0, a1, b0, b1, p0+10e12, p1+10e12)
    total_part2 += 3*tokensA + tokensB

print(f'Part 1: {total_part1}')
print(f'Part 2: {total_part2}')