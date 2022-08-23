import sys

# Gamma and rate
gamma, epsilon = 0, 0

# Input file
infile = open("Day3_input.txt", "r")

# Array to store entries from file
entries = []

# Read file entries into array
for line in infile:
    entries.append(line.strip())
infile.close()

# Loop through entries
l = len(entries[0])
for x in range(l):
    ones = 0
    for n in range(len(entries)):
        if entries[n][x] == '1':
            ones += 1
    if ones > len(entries) / 2:
        gamma += int(2**(l-1-x))
    else:
        epsilon += int(2**(l-1-x))

print("The answer is", gamma*epsilon)
