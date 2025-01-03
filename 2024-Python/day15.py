#!/usr/bin/env python
# Advent Of Code 2024 Day 15 by Craig Brennan
# https://adventofcode.com/2024/day/15

# I have a few ideas on how this code could be simplified but I'm 
# quite proud of this over-engineered mess and it's late

import numpy as np

class MapGrid():
    def __init__(self, map_data, large=False):
        self.robot_y = 0
        self.robot_x = 0
        grid = []
        for y,row in enumerate(map_data.split('\n')):
            new_row = []
            for x,char in enumerate(row):
                if large:
                    match char:
                        case '#':
                            new_row.extend(['#','#'])
                        case '.':
                            new_row.extend(['.','.'])
                        case 'O':
                            new_row.extend(['[',']'])
                        case '@':
                            new_row.extend([char,'.'])
                            self.robot_y, self.robot_x = y, x*2
                else:
                    new_row.append(char)
                    if char == '@':
                        self.robot_y, self.robot_x = y, x
            grid.append(new_row)
        self.grid = np.array(grid)
    
    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

    def get_score(self):
        total = 0
        for y,row in enumerate(self.grid):
            for x,square in enumerate(row):
                if square in ['O', '[']:
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
            if line[0,i] in ['O', '[', ']']:
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
    
    def move_robot_large(self, direction):
        if direction in ['<', '>']:
            self.move_robot(direction)
        elif direction == '^':
            self.can_move = True
            self.to_move = []
            self.search(self.robot_y-1, self.robot_x, -1, True)
            if self.can_move:
                self.to_move.append([self.robot_y,self.robot_x,'@'])
                self.robot_y = self.robot_y - 1
                self.move_squares(self.to_move, -1)
        elif direction == 'v':
            self.can_move = True
            self.to_move = []
            self.search(self.robot_y+1, self.robot_x, 1, True)
            if self.can_move:
                self.to_move.append([self.robot_y,self.robot_x,'@'])
                self.robot_y = self.robot_y + 1
                self.move_squares(self.to_move, 1)

    def search(self, y, x, direction, start=False):
        if y+direction >= len(self.grid): 
            self.can_move = False
            return
        sq = self.grid[y, x]
        next_sq = self.grid[y+direction, x]
        if sq == '.':
            return
        if sq == '#':
            self.can_move = False
            return
        if sq == '[':
            if start:
                self.search(y, x+1, direction)
            if next_sq == '[':
                self.search(y+direction, x, direction)
            elif next_sq == ']':
                self.search(y+direction, x, direction)
                self.search(y+direction, x-1, direction)
            elif next_sq == '#':
                self.can_move = False
        elif sq == ']':
            if start:
                self.search(y,x-1, direction)
            if next_sq == ']':
                self.search(y+direction, x, direction)
            if next_sq == '[':
                self.search(y+direction, x, direction)
                self.search(y+direction, x+1, direction)
            elif next_sq == '#':
                self.can_move = False
        if next_sq != '#' and [y,x,sq] not in self.to_move:
            self.to_move.append([y,x,sq])

    def move_squares(self, squares, direction):
        for square in squares:
            self.grid[square[0]+direction, square[1]] = square[2]
            self.grid[square[0], square[1]] = '.'


data = open('input/day15_input.txt').read().split('\n\n')
grid, large_grid = MapGrid(data[0]), MapGrid(data[0], True)
moves = list(data[1].replace('\n',''))

for move in moves:
    grid.move_robot(move)
    large_grid.move_robot_large(move)

grid.print_grid()
print(f'Part 1: {grid.get_score()}\n') 

large_grid.print_grid()
print(f'Part 2: {large_grid.get_score()}') 