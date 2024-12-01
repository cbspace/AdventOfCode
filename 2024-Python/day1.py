file = open('input/day1_input.txt')
list1, list2 = [], []
total1, total2 = 0, 0

for line in file.readlines():
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

# Part 2
for val in list1:
    total2 += val * list2.count(val)

# Part 1
list1.sort()
list2.sort()

for i in range(len(list1)):
    total1 += abs(list2[i] - list1[i])

print(f'Part1: {total1}')
print(f'Part2: {total2}')