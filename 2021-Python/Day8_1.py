import sys

unique_lengths = [2,3,4,7]
unique_count = 0

input_r = []

infile = open("Day8_input.txt","r")
for l in infile:
    line_data = l.strip()
    line_array = line_data.split(' | ')
    input_r.append(line_array[1].split())

for a in input_r:
    for b in a:
        if unique_lengths.count(len(b)) > 0:
            unique_count += 1

print(unique_count)