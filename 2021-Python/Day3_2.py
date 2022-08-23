import sys

def count(inputs,bit,k):
    ret_val = False
    c=0
    for n in range(len(inputs)):
        if inputs[n][bit] == k:
            c+=1
        if c >= len(inputs) / 2:
            ret_val = True
    return ret_val

def loop(inputs,bit,k):
    ones = 0
    keep = []
    l = len(inputs[0])
    for n in range(len(inputs)):
        if inputs[n][bit] == k:
            keep.append(inputs[n])
    return keep

# Input file
infile = open("Day3_input.txt", "r")

# Array to store entries from file
entries = []
keep = []

# Read file entries into array
for line in infile:
    entries.append(line.strip())
infile.close()

l = len(entries[0])

# Oxygen
keep = entries
for x in range(l):
    if count(keep,x,'1'):
       keep = loop(keep,x,'1')
    else:
        keep = loop(keep,x,'0')
    if len(keep) == 1:
        break
if len(keep) == 2:
    keep = loop(keep,l,'1')
oxygen = int(keep[0],2)

# C02
keep = entries
for x in range(l):
    if count(keep,x,'1'):
       keep = loop(keep,x,'0')
    else:
       keep = loop(keep,x,'1')
    if len(keep) == 1:
        break
c02 = int(keep[0],2)

print("The answer is", oxygen * c02)
