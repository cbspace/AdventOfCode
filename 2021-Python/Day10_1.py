import sys

# Input lines to be parsed
line_array = []

# Stack for parsing
lstack = []

# Valid characters
open_brackets = ['(','[','{','<']
closed_brackets = [')',']','}','>']

# Points
points_table = [3,57,1197,25137]
total_points = 0

# Input file
infile = open("Day10_input.txt", "r")
for l in infile:
	line_array.append(l.strip())

for line in line_array:
	for c in line:
		if c in open_brackets:
			lstack.append(c)
		elif c in closed_brackets:
			if open_brackets[closed_brackets.index(c)] != lstack.pop():
				total_points += points_table[closed_brackets.index(c)]
				continue

print(total_points)
