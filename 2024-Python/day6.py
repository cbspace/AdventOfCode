class MapGrid():
    def __init__(self, map_file):
        self.grid = []
        self.guard_pos = [0,0]
        self.initial_guard_pos = [0,0]
        self.guard_direction = None
        self.guard_codes = ['^', '>', 'v', '<']
        self.guard_delta = [[-1,0], [0,1], [1,0], [0,-1]]
        
        file = open(map_file)

        for y, line in enumerate(file.readlines()):
            self.grid.append(list(line.strip()))
            for x, point in enumerate(line.strip()):
                if point in self.guard_codes:
                    self.guard_pos, self.initial_guard_pos = [y, x], [y, x]
                    self.guard_direction = self.guard_codes.index(point)
                    self.grid[y][x] = 'X'

        file.close()
        self.y_len = len(self.grid)
        self.x_len = len(self.grid[0])

    def get_visited(self):
        visited = []
        for y in range(grid.y_len):
            for x in range(grid.x_len):
                contents = grid.grid[y][x]
                if contents == 'X':
                    visited.append([y,x])
        return visited

    def update_direction_and_check_in_map(self):
        next_clear, in_map = False, True
        already_visited = False

        while not next_clear:
            delta = self.guard_delta[self.guard_direction]
            new_y, new_x = self.guard_pos[0] + delta[0], self.guard_pos[1] + delta[1]
            if 0 <= new_y < self.y_len and 0 <= new_x < self.x_len:
                contents = self.grid[new_y][new_x]
                if contents == '#':
                    self.guard_direction = (self.guard_direction + 1) % 4
                else:
                    self.grid[new_y][new_x] = 'X'
                    if contents == 'X':
                        already_visited = True
                    next_clear = True
            else:
                next_clear = True
                in_map = False

        self.guard_pos = [new_y, new_x]
        return in_map, already_visited

    def check_for_loop(self, obs_y, obs_x):
        in_grid, loop_found = True, False
        unique_pos = self.guard_pos
        self.grid[obs_y][obs_x] = '#'

        while in_grid and not loop_found:
            in_grid, already_visited = self.update_direction_and_check_in_map()
            if not already_visited:
                unique_pos = self.guard_pos
            elif unique_pos == self.guard_pos:
                loop_found = True

        return loop_found

    def print_grid(self):
        for line in self.grid:
            print(''.join(line))

filepath = 'input/day6_input.txt'
grid = MapGrid(filepath)

in_grid = True
while in_grid:
    in_grid, already_visited = grid.update_direction_and_check_in_map()
visited = grid.get_visited()

loops_found = 0
for location in visited:
    if location != grid.initial_guard_pos:
        grid.__init__(filepath)
        if grid.check_for_loop(location[0], location[1]):
            loops_found += 1

print(f'Part 1: {len(visited)}')
print(f'Part 2: {loops_found}')
















































































