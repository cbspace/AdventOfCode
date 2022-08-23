import sys

# Array to store coordinates
coords = []

# Array of paths
path_array = []

# Populate path array
infile = open("Day12_input.txt","r")
for l in infile:
    line_data = l.strip()
    line_array = line_data.split('-')
    coords.append(line_array)

# Create deep copy of array
def array_deep_copy(array_in):
    new_array = []
    for i in array_in:
        new_array.append(i)
    return new_array

# Create array of paths
# cave_in is index of current coordinates
# coord_index = 0 or 1 for current cave
def trace_path(cave_in, coord_index, current_path, travelled, second_visit_done):
    global path_count

    current_cave = coords[cave_in][coord_index]
    new_cave = coords[cave_in][~coord_index]
    current_path.append(current_cave)

    new_travelled = array_deep_copy(travelled)
    if new_cave.islower():
        new_travelled.append(new_cave)

    if new_cave == "end":
        current_path.append("end")
        path_array.append(current_path)
    elif new_cave != "start":
        for c in coords:
            for ci in c:
                if ci == new_cave:
                    if travelled.count(current_cave) == 2:
                        second_visit_done = True
                    if (travelled.count(new_cave) == 0 and second_visit_done) or (travelled.count(new_cave) <= 1 and not second_visit_done) or new_cave.isupper():
                        new_path = array_deep_copy(current_path)
                        trace_path(coords.index(c), c.index(ci), new_path, new_travelled, second_visit_done)
            
# Find the starting points
for c in coords:
    for ci in c:
        if ci == "start":
            current_path = []
            travelled = []
            trace_path(coords.index(c), c.index(ci), current_path, travelled, False)

for a in path_array:
    print(a)

print(len(path_array))