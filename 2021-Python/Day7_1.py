import sys

def test_number(inputs,n):
    t = 0
    for c in inputs:
        t += abs(c - n)
    return t

# Input file
infile = open("Day7_input.txt", "r")

# Array to store entries from file
entries = []
crabs = []

# Read file entries into array
line = infile.readline().strip()
entries = line.split(",")
infile.close()

for a in entries:
    crabs.append(int(a))

t = 0
for a in crabs:
    t += a
average = int(a / len(crabs))

n = 1
a = test_number(crabs,average)
b = test_number(crabs,average+n)

if b < a:
    while b < a:
        n += 1
        a = b
        b = test_number(crabs,average+n)
    c = a
else:
    while b > a:
        n -= 1
        b = a
        a = test_number(crabs,average+n)
    c = b

print(c)


