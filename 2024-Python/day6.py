file = open('input/day6_input.txt')

class MapGrid():
    def __init__(self, map_file):
        self.grid = []
        self.guard_pos = [0,0]
        self.guard_direction = None
        self.guard_codes = ['^', '>', 'v', '<']
        self.guard_delta = [[-1,0], [0,1], [1,0], [0,-1]]
        self.visited = 1
        
        for y, line in enumerate(file.readlines()):
            self.grid.append(list(line.strip()))
            for x, point in enumerate(line.strip()):
                if point in self.guard_codes:
                    self.guard_pos = [y, x]
                    self.guard_direction = self.guard_codes.index(point)
                    self.grid[y][x] = 'X'
        
        self.y_len = len(self.grid)
        self.x_len = len(self.grid[0])

    def update_direction_and_check_in_map(self):
        next_clear, in_map = False, True

        while not next_clear:
            delta = self.guard_delta[self.guard_direction]
            new_y, new_x = self.guard_pos[0] + delta[0], self.guard_pos[1] + delta[1]
            if 0 <= new_y < self.y_len and 0 <= new_x < self.x_len:
                contents = self.grid[new_y][new_x]
                print('Next:', contents, 'Dir:', self.guard_direction)
                if contents == '#':
                    self.guard_direction = (self.guard_direction + 1) % 4
                else:
                    self.grid[new_y][new_x] = 'X'
                    if not contents == 'X':
                        self.visited += 1
                    next_clear = True
            else:
                next_clear = True
                in_map = False

        self.guard_pos = [new_y, new_x]
        return in_map

    def print_grid(self):
        for line in self.grid:
            print(''.join(line))
        print(f'Guard Position: {self.guard_pos}, Direction: {self.guard_direction}')

grid = MapGrid(file)
grid.print_grid()

in_grid = True
while in_grid:
    in_grid = grid.update_direction_and_check_in_map()

grid.print_grid()

print(f'Part1: {grid.visited}')
















































































