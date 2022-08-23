import sys

# X value
x=0

#count
count=0

# map
map_arr = []

# Input file
infile = open('Day3_input.txt', 'r')

# Load file to map
for line in infile:
    map_arr.append(line.strip())
infile.close()

# Loop through array
for map_line in map_arr:
    if map_line[x%len(map_line)]=='#':
        count+=1
    x+=3

print('The answer is',count)
