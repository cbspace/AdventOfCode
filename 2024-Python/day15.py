#!/usr/bin/env python
# Advent Of Code 2024 Day 15 by Craig Brennan
# https://adventofcode.com/2024/day/15

import numpy as np

class MapGrid():
    def __init__(self, map_data):
        self.robot_y = 0
        self.robot_x = 0
        grid = []
        for y,row in enumerate(map_data.split('\n')):
            for x,char in enumerate(row):
                if char == '@':
                    self.robot_y, self.robot_x = y, x
            grid.append([char for char in row])
        self.grid = np.array(grid)
    
    def print_grid(self):
        for row in self.grid:
            print(''.join(row))
        print()

    def get_score(self):
        total = 0
        for y,row in enumerate(self.grid):
            for x,square in enumerate(row):
                if square == 'O':
                    total += 100*y + x
        return total
                

    def move_robot(self, direction):
        # Use some numpy slicification
        match direction:
            case '^':
                dy, dx = -1, 0
                line = self.grid[self.robot_y::-1, self.robot_x:self.robot_x+1].T
            case 'v':
                dy, dx = 1, 0
                line = self.grid[self.robot_y:, self.robot_x:self.robot_x+1].T
            case '<':
                dy, dx = 0, -1
                line = self.grid[self.robot_y:self.robot_y+1, self.robot_x::-1]
            case '>':
                dy, dx = 0, 1
                line = self.grid[self.robot_y:self.robot_y+1, self.robot_x:]
        
        count = 0
        can_move = False
        for i in range(1,len(line[0])):
            if line[0,i] == 'O':
                count += 1
            if line[0,i] == '.':
                count += 1
                can_move = True
                break
            if line[0,i] == '#':
                break
        
        if can_move:
            self.robot_y += dy
            self.robot_x += dx
            for c in range(count,-1,-1):
                if c:
                    line[0,c] = line[0,c-1]
                else:
                    line[0,0] = '.'

data = open('input/test.txt').read().split('\n\n')
grid, large_grid = MapGrid(data[0]), MapGrid(data[0])
moves = list(data[1].replace('\n',''))

for move in moves:
    # print(f'Move {move}:')
    grid.move_robot(move)
    # grid.print_grid()

print(f'Part 1: {grid.get_score()}')