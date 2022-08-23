import sys

# Counter for the answer
count = 0

# Input file
infile = open('Day2_input.txt', 'r')

for line in infile:
    r_pos1 = int(line.split('-')[0])
    r_pos2 = int(line.split('-')[1].split()[0])
    r_char = line.split()[1].split(':')[0]
    r_pwd = line.split()[2].strip()
    if r_pwd[r_pos1-1].count(r_char) + r_pwd[r_pos2-1].count(r_char) == 1:
        count+=1

infile.close()

print('The answer is', count)
