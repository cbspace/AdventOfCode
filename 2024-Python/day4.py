class Grid():
    sp = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

    def __init__(self, buffer):
        self.lines = []
        
        for line in buffer.split('\n'):
            if len(line):
                self.lines.append(line)

        self.y_len = len(self.lines)
        self.x_len = len(self.lines[0])
    
    def load_start_locations(self, start_letter):
        self.word_starts = []
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == start_letter:
                    self.word_starts.append([y, x])

    def get_char(self, point):
        return self.lines[point[0]][point[1]]

    def location_valid(self, point):
        return 0 <= point[0] < self.y_len and 0 <= point[1] < self.x_len

    def get_valid_search_locations(self, point, diag_only=False):
        locations = []
        for i, loc in enumerate(self.sp):
            new_loc = [point[0] + loc[0], point[1] + loc[1]]
            if self.location_valid(new_loc) and (not diag_only or (i+1)%2):
                locations.append(new_loc)
        return locations


file = open('input/day4_input.txt')
grid = Grid(file.read())
grid.load_start_locations('X')
magic_word = 'XMAS'
part1_count, part2_count = 0, 0

for ws in grid.word_starts:
    for sl in grid.get_valid_search_locations(ws):
        if grid.get_char(sl) == magic_word[1]:
            direction = [sl[0]-ws[0], sl[1]-ws[1]]
            third_letter = [sl[0]+direction[0], sl[1]+direction[1]]
            fourth_letter = [sl[0]+direction[0]*2, sl[1]+direction[1]*2]
            
            if (grid.location_valid(third_letter)
                and grid.location_valid(fourth_letter) 
                and grid.get_char(third_letter) == magic_word[2]
                and grid.get_char(fourth_letter) == magic_word[3]):
                part1_count += 1

grid.load_start_locations('A')
magic_word = 'MAS'

for ws in grid.word_starts:
    sl = grid.get_valid_search_locations(ws, diag_only=True)
    if len(sl) == 4:
        char1, char3 = grid.get_char(sl[0]), grid.get_char(sl[2])
        char2, char4 = grid.get_char(sl[1]), grid.get_char(sl[3])
        mas_1 = ((char1 == magic_word[0] and char3 == magic_word[2]) or 
                 (char1 == magic_word[2] and char3 == magic_word[0]))
        mas_2 = ((char2 == magic_word[0] and char4 == magic_word[2]) or 
                 (char2 == magic_word[2] and char4 == magic_word[0]))
        if mas_1 and mas_2:
            part2_count += 1

print('Part 1:', part1_count)
print('Part 2:', part2_count)
