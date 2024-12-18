#!/usr/bin/env python
# Advent Of Code 2024 Day 8 by Craig Brennan
# https://adventofcode.com/2024/day/8

class MapGrid():
    def __init__(self, map_data):
        self.grid1, self.grid2 = [], []
        self.antennas = {}
        self.antinodes1, self.antinodes2 = 0, 0

        for y,line in enumerate(map_data.split('\n')):
            line = line.strip()
            if len(line):
                self.grid1.append([p for p in line])
                self.grid2.append([p for p in line])
                for x,p in enumerate(line):
                    if p != '.':
                        if not p in self.antennas:
                            self.antennas[p] = [[y,x]]
                        else:
                            self.antennas[p].append([y,x])
        self.y_size = len(self.grid1)
        self.x_size = len(self.grid1[0])
    
    def print_grid(self):
        for line in self.grid1:
            print(''.join(line))

    def location_valid(self, loc):
        return 0 <= loc[0] < self.y_size and 0 <= loc[1] < self.x_size

    def update(self, loc, part2=False):
        grid = self.grid2 if part2 else self.grid1

        if grid[loc[0]][loc[1]] != '#':
            grid[loc[0]][loc[1]] = '#'
            if part2:
                self.antinodes2 += 1
            else:
                self.antinodes1 += 1

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
                    grid.update(new_location)

                i = 1
                new_location = [ant1[0], ant1[1]]
                while grid.location_valid(new_location):
                    grid.update(new_location, True)
                    new_location = [ant1[0] - i*delta_y, ant1[1] - i*delta_x]
                    i = i + 1

grid.print_grid()
print(f'Part 1: {grid.antinodes1}')
print(f'Part 2: {grid.antinodes2}')