import sys

# Counter for the answer
count = 0

# Input file
infile = open('Day2_input.txt', 'r')

for line in infile:
    r_min = int(line.split('-')[0])
    r_max = int(line.split('-')[1].split()[0])
    r_char = line.split()[1].split(':')[0]
    r_pwd = line.split()[2].strip()
    if r_min <= r_pwd.count(r_char) <= r_max:
        count+=1

infile.close()

print('The answer is', count)
