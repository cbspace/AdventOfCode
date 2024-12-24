#!/usr/bin/env python
# Advent Of Code 2024 Day 10 by Craig Brennan
# https://adventofcode.com/2024/day/10

class Grid():
    def __init__(self, filename):
        file = open(filename)
        self.grid = []
        self.start_locations = []

        for y,line in enumerate(file.readlines()):
            row = []
            for x,point in enumerate(line.strip()):
                row.append(int(point))
                if int(point) == 0:
                    self.start_locations.append([y,x])
            self.grid.append(row)
        
        self.height = len(self.grid)
        self.width = len(self.grid[0])
    
    def square_valid(self, point):
        return 0 <= point[0] < self.height and 0 <= point[1] < self.width

    def print_grid(self):
        for row in self.grid:
            print(row)


grid = Grid('input/test.txt')
grid.print_grid()

start = grid.start_locations[0]
