#!/usr/bin/env python
# Advent Of Code 2024 Day 8 by Craig Brennan
# https://adventofcode.com/2024/day/8

class MapGrid():
    def __init__(self, map_data):
        self.grid = []
        self.antennas = {}
        self.antinodes = 0

        for y,line in enumerate(map_data.split('\n')):
            line = line.strip()
            if len(line):
                self.grid.append([p for p in line])
                for x,p in enumerate(line):
                    if p != '.':
                        if not p in self.antennas:
                            self.antennas[p] = [[y,x]]
                        else:
                            self.antennas[p].append([y,x])
        self.y_size = len(self.grid)
        self.x_size = len(self.grid[0])
    
    def print_grid(self):
        for line in self.grid:
            print(''.join(line))

    def location_valid(self, loc):
        return 0 <= loc[0] < self.y_size and 0 <= loc[1] < self.x_size

    def update(self, loc, val):
        if self.grid[loc[0]][loc[1]] != '#':
            self.antinodes += 1
            self.grid[loc[0]][loc[1]] = val


file_data = open('input/day8_input.txt').read()
grid = MapGrid(file_data)

for antenna_group in grid.antennas.keys():
    antennas = grid.antennas[antenna_group]
    for idx1 in range(len(antennas)):
        ant1 = antennas[idx1]
        for idx2 in range(len(antennas)):
            if not idx2 == idx1:
                ant2 = antennas[idx2]
                delta_y = ant2[0] - ant1[0]
                delta_x = ant2[1] - ant1[1]
                new_location = [ant1[0] - delta_y, ant1[1] - delta_x]
                if grid.location_valid(new_location):
                    grid.update(new_location, '#')

grid.print_grid()
print(f'Part 1: {grid.antinodes}')