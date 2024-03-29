#!/usr/bin/python3

infile = open("input/day2_input.txt","r")
cubes = {"red": 12, "green": 13, "blue": 14}

games = []
game_sum, power_sum = 0, 0

for l in infile:
    game_array = []
    split_colon = l.strip().split(": ")
    game_id = int(split_colon[0].split()[1])
    game_array.append(game_id)

    split_games = split_colon[1].split("; ")
    game_array.append(split_games)
    games.append(game_array)
    
infile.close()

for g in games:
    possible = True
    min_red, min_green, min_blue = 0, 0, 0
    for game_set in g[1]:
        cube_strs = game_set.split(", ")
        for c in cube_strs:
            number, colour = int(c.split()[0]), c.split()[1]
            min_red = number if colour == "red" and number > min_red else min_red
            min_green = number if colour == "green" and number > min_green else min_green
            min_blue = number if colour == "blue" and number > min_blue else min_blue
            if number > cubes[colour]:
                possible = False
    if possible:
        game_sum += g[0]

    power_sum += min_red * min_green * min_blue

print("Part 1:" , game_sum)
print("Part 2:" , power_sum)