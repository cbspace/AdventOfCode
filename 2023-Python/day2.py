#!/usr/bin/python3

import sys

infile = open("input/day2_input.txt","r")
cubes = {"red": 12, "green": 13, "blue": 14}

games = []
game_sum, power_sum = 0, 0

def process_game(str_in):
    game_aray = []
    split_colon = str_in.split(": ")
    game_id = int(split_colon[0].split()[1])
    game_aray.append(game_id)

    split_games = split_colon[1].split("; ")
    game_aray.append(split_games)
    return game_aray

for l in infile:
    games.append(process_game(l.strip()))

infile.close()

for g in games:
    possible = True
    min_red, min_green, min_blue = 0, 0, 0
    for game_set in g[1]:
        cube_strs = game_set.split(", ")
        for c in cube_strs:
            number, colour = int(c.split()[0]), c.split()[1]
            if number > cubes[colour]:
                possible = False
            if colour == "red" and number > min_red:
                min_red = number
            elif colour == "green" and number > min_green:
                min_green = number
            elif colour == "blue" and number > min_blue:
                min_blue = number
    if possible:
        game_sum += g[0]

    power_sum += min_red * min_green * min_blue

print("Part 1:" , game_sum)
print("Part 2:" , power_sum)