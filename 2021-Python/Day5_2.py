import sys

# Input file
infile = open("Day5_input.txt", "r")

# Array to store entries from file
entries = []

# The diagram initally zeros
s = 1000
diagram = [[0 for x in range(s)] for y in range(s)]

# Read file entries into array [[x1,y1],[x2,y2]]
for line in infile:
    line2 = line.strip().replace(" -> ",",").split(",")
    for e in range(0,len(line2),4):
        point = [[int(line2[e]),int(line2[e+1])],[int(line2[e+2]),int(line2[e+3])]]
        entries.append(point)
infile.close()

for p in entries:
    # Draw along y
    if p[0][0] == p[1][0]:
        if p[0][1] < p[1][1]:                       #y0 < y1
            for y in range(p[0][1],p[1][1]+1):
                diagram[y][p[0][0]] += 1
        else:                                       #y0 >= y1
            for y in range(p[1][1],p[0][1]+1):
                diagram[y][p[0][0]] += 1
    # Draw along x
    elif p[0][1] == p[1][1]:
        if p[0][0] < p[1][0]:                       #x0 < x1
            for x in range(p[0][0],p[1][0]+1):
                diagram[p[0][1]][x] += 1
        else:                                       #x0 > x1
            for x in range(p[1][0],p[0][0]+1):
                diagram[p[0][1]][x] += 1
    # Draw diagonal
    else:
        if p[0][0] < p[1][0]:                        #x0 < x1 &
            if p[0][1] < p[1][1]:                    #y0 < y1
                for c in range(p[1][0]-p[0][0]+1):
                        diagram[p[0][1]+c][p[0][0]+c] += 1
            else:                                    #y0 > y1
                for c in range(p[1][0]-p[0][0]+1):
                        diagram[p[0][1]-c][p[0][0]+c] += 1
        else:                                        #x0 > x1 &
            if p[0][1] < p[1][1]:                    #y0 < y1
                for c in range(p[0][0]-p[1][0]+1):
                        diagram[p[0][1]+c][p[0][0]-c] += 1
            else:                                    #y0 > y1
                for c in range(p[0][0]-p[1][0]+1):
                        diagram[p[0][1]-c][p[0][0]-c] += 1

total = 0
for r in diagram:
    for c in r:
        if c > 1:
            total += 1

print("The answer is", total)



