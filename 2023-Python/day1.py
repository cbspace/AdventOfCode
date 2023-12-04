#!/usr/bin/python3

infile = open("input/day1_input.txt","r")

calibration_sum_1, calibration_sum_2 = 0, 0

def find_number(in_str):
    valid_strings = ["one","two","three","four","five","six","seven","eight","nine"]
    for s in valid_strings:
        number_index = in_str.find(s)
        if number_index == 0:
            return valid_strings.index(s) + 1
    return -1

for line in infile:
    line_str = line.strip()

    for char in line_str:
        if char.isdigit():
            first_digit_part1 = char
            break
        
    for char in reversed(line_str):
        if char.isdigit():
            last_digit_part1 = char
            break

    for i, char in enumerate(line_str):
        if (n := find_number(line_str[i:])) != -1:
            first_digit_part2 = str(n)
            break
        elif char.isdigit():
            first_digit_part2 = char
            break

    for i, char in enumerate(reversed(line_str)):
        if (n := find_number(line_str[len(line_str) - i:])) != -1:
            last_digit_part2 = str(n)
            break
        elif char.isdigit():
            last_digit_part2 = char
            break

    calibration_sum_1 += int(first_digit_part1 + last_digit_part1)
    calibration_sum_2 += int(first_digit_part2 + last_digit_part2)

infile.close()

print("Part 1: ", calibration_sum_1)
print("Part 2: ", calibration_sum_2)
