#!/usr/bin/python3

infile = open("input/day3_input.txt","r")
sch = []
num_adj_gear_list = []
parts_sum = 0
gear_ratio_sum = 0

for l in infile:
    sch.append(l.strip())

infile.close()

y_max = len(sch) - 1
x_max = len(sch[0]) - 1

def symbol_adjacent(y, x):
    symbol_found, gear_found = False, False
    gear_location_y, gear_location_x = 0, 0
    adj_squares = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

    for sq in adj_squares:
        y_val = y + sq[0]
        x_val = x + sq[1]
        if y_val >= 0 and x_val >= 0 and y_val < y_max and x_val < x_max:
            symbol_found = not(sch[y_val][x_val].isdigit() or sch[y_val][x_val]==".") or symbol_found
            if symbol_found and sch[y_val][x_val]=="*":
                gear_found, gear_location_y, gear_location_x = True, y_val, x_val

    return symbol_found, gear_found, gear_location_y, gear_location_x

y = 0
number_str = ""
symbol_found, gear_found = False, False
gear_location_y, gear_location_x = 0, 0

for line in sch:
    if len(number_str) > 0:
        if symbol_found:
            if gear_found:
                list_index = -1
                for i, n in enumerate(num_adj_gear_list):
                    if n[0] == gear_location_y and n[1] == gear_location_x:
                        list_index = i
                        break
                if list_index == -1:
                    num_adj_gear_list.append([gear_location_y, gear_location_x,[int(number_str)]])
                else:
                    num_adj_gear_list[i][2].append(int(number_str))
            symbol_found, gear_found = False, False
        number_str = ""

    for x, c in enumerate(line):
        if c.isdigit():
            number_str += c
            symbol_found_new, gear_found_new, gear_location_y_new, gear_location_x_new = symbol_adjacent(y,x)
            symbol_found = symbol_found_new or symbol_found
            gear_found = gear_found_new or gear_found
            gear_location_y = gear_location_y_new or gear_location_y
            gear_location_x = gear_location_x_new or gear_location_x
        else:
            if len(number_str) > 0:
                if symbol_found:
                    parts_sum += int(number_str)
                    if gear_found:
                        list_index = -1
                        for i, n in enumerate(num_adj_gear_list):
                            if n[0] == gear_location_y and n[1] == gear_location_x:
                                list_index = i
                                break
                        if list_index == -1:
                            num_adj_gear_list.append([gear_location_y, gear_location_x,[int(number_str)]])
                        else:
                            num_adj_gear_list[i][2].append(int(number_str))
                    symbol_found, gear_found = False, False
                number_str = ""

    y += 1

for g in num_adj_gear_list:
    if len(g[2]) == 2:
        gear_ratio_sum += g[2][0] * g[2][1]

print("Part 1", parts_sum)
print("Part 2", gear_ratio_sum)