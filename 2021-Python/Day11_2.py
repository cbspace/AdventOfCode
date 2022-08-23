import sys

# Array to store octopus map from file
omap = []

# Coordinates used to find adjacent (y,x)
adj_coord = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

# Flash total
flash_total = 0

# Number of steps
steps = 0

# Input file
infile = open("Day11_input.txt", "r")

for l in infile:
	line_array = []
	line = l.strip()
	for x in line:
		line_array.append(int(x))
	omap.append(line_array)
	
# Maximum loop values
xmax = len(omap[0])
ymax = len(omap)

# Recursive function to do a single do_step
def do_step(y,x):
	global flash_total
	global omap, flash_map
	if omap[y][x] == 9:
		omap[y][x] = 0
		flash_map[y][x] = True
		flash_total += 1
		adj_list = find_adjacent(y,x)
		for a in adj_list:
			do_step(a[0],a[1])
	elif flash_map[y][x] == False:
		omap[y][x] += 1
		
# Find adjacent coordinates and return as a list
def find_adjacent(y,x):
	valid_coords = []
	for a in adj_coord:
		y1 = a[0] + y
		x1 = a[1] + x
		if y1 >= 0 and y1 < ymax and x1 >= 0 and x1 < xmax:
			valid_coords.append([y1,x1])
	return valid_coords

while(True):
	steps += 1
	# Reset flash_map and total flashes
	flash_map = []
	flash_total = 0
	for g in range(ymax):
		flash_line = [False] * xmax
		flash_map.append(flash_line)
	flash_line = [False] * xmax
	# Loop through octupus map
	for cy in range(ymax):
		for cx in range(xmax):
			do_step(cy,cx)
	if flash_total == ymax * xmax:
		print(steps)
		break
