import sys

depth = 0
horizontal = 0

# Input file
infile = open("C:/code/input.txt", "r")

# Loop through file
for line in infile:
    if line.split()[0] == 'forward':
        horizontal+=int(line.split()[1])
    elif line.split()[0] == 'up':
        depth-=int(line.split()[1])
    elif line.split()[0] == 'down':
        depth+=int(line.split()[1])
    
infile.close()

print("The answer is", depth*horizontal)