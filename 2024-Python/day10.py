#!/usr/bin/env python
# Advent Of Code 2024 Day 10 by Craig Brennan
# https://adventofcode.com/2024/day/10

class Grid():
    def __init__(self, filename):
        file = open(filename)
        self.adjacents = [[-1,0], [0,1], [1,0], [0,-1]]
        self.grid = []
        self.start_locations = []
        self.part1_score = 0
        self.part2_score = 0

        for y,line in enumerate(file.readlines()):
            row = []
            for x,point in enumerate(line.strip()):
                row.append(int(point))
                if int(point) == 0:
                    self.start_locations.append([y,x])
            self.grid.append(row)
        
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def get_value(self, point):
        return self.grid[point[0]][point[1]]
    
    def square_valid(self, point):
        return 0 <= point[0] < self.height and 0 <= point[1] < self.width

    # Search recursively
    def search(self, search_loc, ends_found):
        current_value = self.get_value(search_loc)

        for adj in self.adjacents:
            new_y = search_loc[0] + adj[0]
            new_x = search_loc[1] + adj[1]
            new_location = [new_y, new_x]
            if self.square_valid(new_location):
                new_value = self.get_value(new_location)
                if new_value == current_value + 1:
                    if new_value == 9: 
                        if not new_location in ends_found:
                            ends_found.append(new_location)
                            self.part1_score += 1
                        self.part2_score += 1
                    else:
                        self.search(new_location, ends_found)

grid = Grid('input/day10_input.txt')
for start_loc in grid.start_locations:
    grid.search(start_loc, [])

print(f'Part 1: {grid.part1_score}')
print(f'Part 2: {grid.part2_score}')