import sys

# Array to store height map from file
hmap = []

# Risk level total
r_level_total = 0

# Input file
infile = open("Day9_input.txt", "r")

for l in infile:
	line_array = []
	line = l.strip()
	for x in line:
		line_array.append(int(x))
	hmap.append(line_array)

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

# Maximum loop values
xmax = len(hmap[0])
ymax = len(hmap)

for y in range(ymax):
	for x in range(xmax):
		r_level_total += check_for_basin(y,x)

# Print the answer
print(r_level_total)

