#!/usr/bin/env python
# Advent Of Code 2024 Day 14 by Craig Brennan
# https://adventofcode.com/2024/day/14

import numpy as np

class Robot():
    def __init__(self, x, y, vx, vy):
        self.y = y
        self.x = x
        self.vy = vy
        self.vx = vx

    def move(self, w, h):
        new_y = self.y + self.vy
        new_x = self.x + self.vx
        if new_y >= h:
            new_y %= h
        elif new_y < 0:
            new_y = h - abs(new_y)%h
        if new_x >= w:
            new_x %= w
        elif new_x < 0:
            new_x = w - abs(new_x)%w
        self.y = new_y
        self.x = new_x

def generate_grid(robots, w, h):
    grid = [[0 for width in range(w)] for height in range(h)]
    for robot in robots:
        grid[robot.y][robot.x] += 1
    return grid

def count_score(grid):
    my = len(grid) // 2
    mx = len(grid[0]) // 2
    g = np.array(grid)
    quads = [g[:my,:mx], g[:my,mx+1:], g[my+1:,:mx], g[my+1:,mx+1:]]
    total = 1
    for q in [q.sum() for q in quads]:
        total *= q
    return(total)

def draw_map(grid, t=0):
    buffer = f'After {t} seconds:\n'
    for i,line in enumerate(grid):
        s = f''
        for square in line:
            s += str(square).replace('0', '.')
        buffer += s + '\n'
    return buffer + '\n'

file = open('input/day14_input.txt')
width, height = 101, 103
robots = []

for line in file.readlines():
    data = line[2:].strip().split(' v=')
    x, y = [int(n) for n in data[0].split(',')]
    vx, vy = [int(n) for n in data[1].split(',')]
    new_robot = Robot(x, y, vx, vy)
    robots.append(new_robot)

# For part 2 I manually searched for the tree in the output file. I noticed a tree starting to
# form at 27 seconds and 128 seconds. With that I mind I modified my program to only print the 
# grid at times matching T-27 % 101 == 0. Looking through these outputs yielded the tree!

outfile = open('day13_treefile.txt', 'w')
for i in range(1,10_000):
    for robot in robots:
        robot.move(width, height)
    if i == 100:
        part1_total = count_score(generate_grid(robots, width, height))
    if (i-27) % 101 == 0:
        outfile.write(draw_map(generate_grid(robots, width, height),i))
outfile.close()

print(f'Part 1: {part1_total}')
print(f'Part 2: File generated! You will find the tree at 8006 seconds!')

