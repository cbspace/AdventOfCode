import sys

# Counter for the answer
counter = 0

# Input file
infile = open("Day1_input.txt", "r")

# Initialise previous
previous = int(infile.readline())

# Read file entries
for line in infile:
    current = int(line)
    if current > previous:
        counter += 1
    previous = current
infile.close()

print("The answer is", counter)
