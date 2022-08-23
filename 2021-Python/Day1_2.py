import sys

# Counter for the answer
counter = 0

# Input file
infile = open("Day1_input.txt", "r")

# Array to store entries from file
entries = []

# Read file entries into array
for line in infile:
    entries.append(int(line))
infile.close()

# Initialise previous
prev_total = entries[0] + entries[1] + entries[2]

# Loop through entries
for x in range(3,len(entries)):
    new_total = entries[x-2] + entries[x-1] + entries[x]
    if new_total > prev_total:
        counter+=1
    prev_total = new_total

print("The answer is", counter)
