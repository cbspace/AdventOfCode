import sys

# Input file
infile = open("Day6_input1.txt", "r")

# Array to store entries from file
entries = []
fish = []

days = 28

# Read file entries into array
line = infile.readline().strip()
entries = line.split(",")
infile.close()

for e in entries:
    fish.append(int(e))

for d in range(days):
    for f in range(len(fish)):
        if fish[f] == 0:
            fish[f] = 6
            fish.append(8)
        else:
            fish[f] -= 1

print(days)
print(fish)
print(len(fish))
