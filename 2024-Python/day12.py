#!/usr/bin/env python
# Advent Of Code 2024 Day 12 by Craig Brennan
# https://adventofcode.com/2024/day/12

class Region():
    def __init__(self, ident):
        self.identifier = ident
        self.start_loc = []
        self.area = 0
        self.perimeter = []
        self.sides = 0

class MapGrid():
    def __init__(self, file):
        self.grid = []
        self.visited = []
        self.regions = []
        self.search = [[-1,0], [0,1], [1,0], [0,-1]]
        # 0 - Left/Down, 1 - Right/Bottom, 2 - Up/Right, 3 - Top/Left
        self.search_corners = [[1,0], [1,-1]], [[0,1], [1,1]], [[-1,0], [-1,1]], [[0,-1], [-1,-1]]

        for y, line in enumerate(file.readlines()):
            line = line.strip()
            self.grid.append(line)
            self.visited.append([False for x in range(len(line))])

        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def location_valid(self, loc, check_visited=True):
        return (0 <= loc[0] < self.height and 0 <= loc[1] < self.width 
               and (not self.visited[loc[0]][loc[1]] or not check_visited))

    def get_first_not_visited(self):
        for y, line in enumerate(self.grid):
            for x, square in enumerate(line):
                if not self.visited[y][x]:
                    return [y, x]
        return [-1, -1]

    def get_perimeter(self, loc, region):
        for i,search_loc in enumerate(self.search):
            new_y = loc[0] + search_loc[0]
            new_x = loc[1] + search_loc[1]
            if self.location_valid([new_y,new_x], check_visited=False):
                if self.grid[new_y][new_x] != region.identifier:
                    region.perimeter.append([loc[0], loc[1], 3-i, False])
            else:
                region.perimeter.append([loc[0], loc[1], 3-i, False])

    def get_next_side_not_visited(self, region):
        for side in region.perimeter:
            if side[3] == False:
                return False, side
        return True, []

    def trace_sides(self, region):
        done, current_side = self.get_next_side_not_visited(region)
        current_side[3] = True
        turn, next_side = self.get_next_side(current_side, region.identifier)
        region.sides += turn

        while not done:
            if next_side[3] == True:
                done, next_side = self.get_next_side_not_visited(region)
                if done: break
            current_side = next_side
            next_side[3] = True
            turn, next_side = self.get_next_side(current_side, region.identifier)
            region.sides += turn

    def get_next_side(self, current_side, ident):
        turn = 0
        search_pattern = self.search_corners[current_side[2]]
        match_grid = [False, False]

        for i,search in enumerate(search_pattern):
            new_y = current_side[0] + search[0]
            new_x = current_side[1] + search[1]
            if self.location_valid([new_y,new_x],False):
                new_value = self.grid[new_y][new_x]
                if new_value == ident:
                    match_grid[i] = True
        
        if match_grid[0] == False:
            next_direction = (current_side[2] + 1) % 4
            next_square = [current_side[0], current_side[1]]
            turn = 1
        elif match_grid == [True, True]:
            next_direction = current_side[2] - 1
            if next_direction == -1: next_direction = 3
            turn = 1
            next_square = [current_side[0] + search_pattern[1][0], current_side[1] + search_pattern[1][1]]
        else:
            next_square = [current_side[0] + search_pattern[0][0], current_side[1] + search_pattern[0][1]]
            next_direction = current_side[2]
        
        return turn, [next_square[0], next_square[1], next_direction, current_side[3]]

    def explore(self, start_loc):
        ident = self.grid[start_loc[0]][start_loc[1]]
        region = Region(ident)
        region.start_loc = start_loc
        q = [start_loc]
        local_visited = []

        while len(q):
            current_loc = q.pop(0)
            current_value = self.grid[current_loc[0]][current_loc[1]]
            local_visited.append(current_loc)
            self.visited[current_loc[0]][current_loc[1]] = True
            region.area += 1
            self.get_perimeter(current_loc, region)
            for search_loc in self.search:
                new_y = current_loc[0] + search_loc[0]
                new_x = current_loc[1] + search_loc[1]
                if self.location_valid([new_y,new_x]) and not [new_y,new_x] in local_visited:
                    new_value = self.grid[new_y][new_x]
                    if new_value == current_value and not [new_y,new_x] in q:
                        q.append([new_y, new_x])

        self.regions.append(region)

file = open('input/day12_input.txt')
grid = MapGrid(file)
part1_score, part2_score = 0, 0

while (start_loc := grid.get_first_not_visited()) != [-1,-1]:
    grid.explore(start_loc)

for r in grid.regions:
    part1_score += r.area * len(r.perimeter)
    grid.trace_sides(r)
    part2_score += r.area * r.sides

print(f'Part 1: {part1_score}')
print(f'Part 2: {part2_score}')