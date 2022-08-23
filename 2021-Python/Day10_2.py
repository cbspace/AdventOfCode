import sys

# Input lines to be parsed
line_array = []

# Valid characters
open_brackets = ['(','[','{','<']
closed_brackets = [')',']','}','>']

# Points
points_table = []

# Input file
infile = open("Day10_input.txt", "r")
for l in infile:
	line_array.append(l.strip())

for line in line_array:
	lstack = []
	total_points = 0
	corrupt = False
	for c in line:
		if c in open_brackets:
			lstack.append(c)
		elif c in closed_brackets:
			if open_brackets[closed_brackets.index(c)] != lstack.pop():
				corrupt = True
				continue
	if not corrupt:
		for s in reversed(lstack):
			total_points *= 5
			total_points += open_brackets.index(s)+1
		points_table.append(total_points)

points_table.sort()
print(points_table[int((len(points_table)-1)/2)])
