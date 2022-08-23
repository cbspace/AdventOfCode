import sys
import math

# Input file
infile = open("Day6_input.txt", "r")

# Array to store entries from file
entries = []
fish_i = []
n_fish = [0,0,0,0,0,0,0,0,0]

days = 256

# Read file entries into array
line = infile.readline().strip()
entries = line.split(",")
infile.close()

# Convert to int
for e in entries:
    fish_i.append(int(e))

# Count the fishes
for f in fish_i:
    n_fish[f] += 1

# Loop days and update arrays
for d in range(days):
    z = n_fish.pop(0)
    n_fish[6] += z
    n_fish.append(z)

# Calculate total fish
t = 0
for x in n_fish:
    t += x

# Print the answer
print(t)
