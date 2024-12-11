file = open('input/day5_input.txt')

number_list = []
run_list = []
reached_blank = False

part1_total = 0

for line in file.readlines():
    line = line.strip()

    if not len(line):
        reached_blank = True
        continue

    if not reached_blank:
        number_list.append((line[:2], line[3:]))
    else:
        pages = line.split(',')
        pages_dict = {x:i for i,x in enumerate(pages)}
        pages_dict['middle'] = int(pages[len(pages)//2])
        run_list.append(pages_dict)

for update in run_list:
    success = True
    for a,b in number_list:
        if a in update and b in update:
            if not update[a] < update[b]:
                success = False
    if success:
        part1_total += update['middle']

print(f'Part 1: {part1_total}')
