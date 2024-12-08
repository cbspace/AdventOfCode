from enum import Enum

class Directions(Enum):
    Undef  =  0
    Up     =  1
    Down   =  2

def get_direction(a, b):
    if a == b:
        return Directions.Undef
    elif a < b:
        return Directions.Up
    else:
        return Directions.Down

def is_valid(direction, a, b):
    if a == b:
        return False

    match direction:
        case Directions.Up:
            difference = b - a
            if not (difference >=1 and difference <= 3):
                return False
        case Directions.Down:
            difference = a - b
            if not (difference >=1 and difference <= 3):
                return False

    return True

def test_for_pass(report):
    direction = Directions.Undef
    previous = report[0]

    for idx in range(1, len(report)):
        current = report[idx]
        if direction == Directions.Undef:
            direction = get_direction(previous, current)

        if not is_valid(direction, previous, current):
            return False

        previous = current
    return True

file = open('input/day2_input.txt')
part1_count, part2_count = 0, 0

for line in file.readlines():
    report = [int(x) for x in line.split()]
    passed = test_for_pass(report)
    if passed:
        part1_count += 1
        part2_count += 1
    else:
        errors = 0
        for i in range(len(report)):
            report_short = [report[j] for j in range(len(report)) if j != i]
            passed = test_for_pass(report_short)
            if passed:
                part2_count += 1
                break

print(f'Part 1: {part1_count}')
print(f'Part 2: {part2_count}')
