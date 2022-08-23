import sys

# Array to store height map from file
hmap = []
# Grid map indicating True if site already counted
check_map = []

# Array to store 3 largest basins
largest = [0,0,0]

# Input file
infile = open("Day9_input.txt", "r")

# Populate height map and check map arrays
for l in infile:
	line_array = []
	line = l.strip()
	check_map_line = []
	for x in line:
		line_array.append(int(x))
		check_map_line.append(False)
	hmap.append(line_array)
	check_map.append(check_map_line)

# Function to find basin low point
def check_for_basin(y,x):
	r_level = 0
	current = hmap[y][x]
	if x == 0:
		x0 = 10
	else:
		x0 = hmap[y][x-1]
	if x == xmax-1:
		x1 = 10
	else:
		x1 = hmap[y][x+1]
	if y == 0:
		y0 = 10
	else:
		y0 = hmap[y-1][x]
	if y == ymax-1:
		y1 = 10
	else:
		y1 = hmap[y+1][x]

	if current < x0 and current < x1 and current < y0 and current < y1:
		r_level += current + 1
		return r_level
	else:
		return 0

# Function to find size of basin
def find_basin_size(y,x):
	global basin_size
	current = hmap[y][x]
	if x == 0:
		x0 = 10
	else:
		x0 = hmap[y][x-1]
	if x == xmax-1:
		x1 = 10
	else:
		x1 = hmap[y][x+1]
	if y == 0:
		y0 = 10
	else:
		y0 = hmap[y-1][x]
	if y == ymax-1:
		y1 = 10
	else:
		y1 = hmap[y+1][x]
	
	check_map[y][x] = True
	if y0 < 9 and y0 >= current:
		if check_map[y-1][x] == False:
			check_map[y-1][x] = True
			basin_size += 1
			find_basin_size(y-1,x)
	if x0 < 9 and x0 >= current:
		if check_map[y][x-1] == False:
			check_map[y][x-1] = True
			basin_size += 1
			find_basin_size(y,x-1)
	if y1 < 9 and y1 >= current:
		if check_map[y+1][x] == False:
			check_map[y+1][x] = True
			basin_size += 1
			find_basin_size(y+1,x)
	if x1 < 9 and x1 >= current:
		if check_map[y][x+1] == False:
			check_map[y][x+1] = True
			basin_size += 1
			find_basin_size(y,x+1)

# Maximum values
xmax = len(hmap[0])
ymax = len(hmap)

for y in range(ymax):
	for x in range(xmax):
		if check_for_basin(y,x) != 0:
			basin_size = 1
			find_basin_size(y,x)
			if basin_size > largest[0]:
				largest[0] = basin_size
				largest.sort()

# Print the answer
print(str(largest[0]*largest[1]*largest[2]))
