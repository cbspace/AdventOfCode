import sys

# Array to store entries from file
entries = []

# Input file
infile = open("Day1_input.txt", 'r')

# Load file to entries
for line in infile:
    entries.append(int(line))
infile.close()

# Find Part 1 Answer
for x in range(len(entries)):
    for y in range(x+1, len(entries)):
        if entries[x] + entries[y] == 2020:
            print("Part 1 Answer:", entries[x]*entries[y])

# Find Part 2 Answer
for x in range(len(entries)):
    for y in range(x+1, len(entries)):
        for z in range(y+1, len(entries)):
            if entries[x] + entries[y] + entries[z]  == 2020:
                print("Part 2 Answer:", entries[x]*entries[y]*entries[z])
