file = open('input/day3_input.txt')
buffer = file.read()

def process_string(str_in):
    total = 0

    filter1 = str_in.split('mul(')

    for item in filter1:
        split_on_comma = item.split(',')

        if len(split_on_comma) > 1 and split_on_comma[1].count(')'):
            if split_on_comma[0].isnumeric():
                split_on_bracket = split_on_comma[1].split(')')
                if split_on_bracket[0].isnumeric():
                    total += int(split_on_comma[0]) * int(split_on_bracket[0])

    return total

part2_total = 0
split_dont = buffer.split("don't()")
part2_total += process_string(split_dont[0])

for idx in range(1, len(split_dont)):
    split_do = split_dont[idx].split('do()')
    if len(split_do) > 1:
        for i in range(1, len(split_do)):
            part2_total += process_string(split_do[i])

print(f'Part 1: {process_string(buffer)}')
print(f'Part 2: {part2_total}')        