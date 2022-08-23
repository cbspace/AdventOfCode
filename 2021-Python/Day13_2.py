import sys

# Array to store coordinates from file (y,x)
coords = []

# Array to store folds from file
folds = []

# Array to store paper map
pmap = []

# Input file
infile = open("Day13_input.txt", "r")

for l in infile:
	line = l.strip()
	if line.count(',') > 0:
		coords.append([int(line.split(',')[1]),int(line.split(',')[0])])
	elif line[:4] == 'fold':
		folds.append([line[11],int(line.split('=')[1])])

# Create blank paper at appropriate size
y_max = sorted(coords, key=lambda row: (row[0]))[-1][0]
x_max = sorted(coords, key=lambda row: (row[1]))[-1][1]

for y in range(y_max+1):
	pmap_line = []
	for x in range(x_max+1):
		pmap_line.append('.')
	pmap.append(pmap_line)

# Add coordinates
for c in coords:
	pmap[c[0]][c[1]] = "#"

# Fold on the x-axis
def foldx(p_input,fold_val):
	f_pmap = []
	for y in range(len(p_input)):
		f_pmap.append(p_input[y][:fold_val])
		for x in range(fold_val+1,len(p_input[0])):
			z = p_input[y][x]
			if z == '#':
				f_pmap[y][fold_val-x] = z
	return f_pmap
	
# Fold on the y-axis
def foldy(p_input,fold_val):
	f_pmap = p_input[:fold_val]
	for y in range(fold_val+1,len(p_input)):
		for x in range(len(p_input[0])):
			z = p_input[y][x]
			if z == '#':
				f_pmap[fold_val-y][x] = z
	return f_pmap

# Do the folds
folded = pmap
for f in folds:
	if f[0] == 'x':
		folded = foldx(folded,f[1])
	elif f[0] == 'y':
		folded = foldy(folded,f[1])

for y in range(len(folded)):
	print(''.join(folded[y]))
