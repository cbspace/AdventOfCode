#include <fstream>
#include <iostream>
#include <string>

using namespace std;

enum class GameShape {
    Rock = 1,
    Paper = 2,
    Scissors = 3
};

enum class GameOutcome {
    Lose = 0,
    Draw = 3,
    Win = 6
};

struct Game {
    GameShape my_shape;
    GameShape opponent_shape;
    GameOutcome outcome;
};

GameOutcome get_outcome(GameShape, GameShape);
GameShape get_my_shape(GameShape, GameOutcome);

int main(int, char**) {
    fstream ifs;
    string line_str;
    int part1_score, part2_score = 0;

    ifs.open("input/day2_input.txt", ios::in);

    while (!ifs.eof()) {
        Game part1_this_game, part2_this_game;

        getline(ifs, line_str);
        if (line_str.empty())
            break;

        switch (line_str[0]) {
            case 'A':
                part1_this_game.opponent_shape = GameShape::Rock;
                part2_this_game.opponent_shape = GameShape::Rock;
                break;
            case 'B':
                part1_this_game.opponent_shape = GameShape::Paper;
                part2_this_game.opponent_shape = GameShape::Paper;
                break;
            case 'C':
                part1_this_game.opponent_shape = GameShape::Scissors;
                part2_this_game.opponent_shape = GameShape::Scissors;
                break;
        }

        switch (line_str[2]) {
            case 'X':
                part1_this_game.my_shape = GameShape::Rock;
                part2_this_game.outcome = GameOutcome::Lose;
                break;
            case 'Y':
                part1_this_game.my_shape = GameShape::Paper;
                part2_this_game.outcome = GameOutcome::Draw;
                break;
            case 'Z':
                part1_this_game.my_shape = GameShape::Scissors;
                part2_this_game.outcome = GameOutcome::Win;
                break;
        }

        part1_this_game.outcome = get_outcome(part1_this_game.my_shape, part1_this_game.opponent_shape);
        part1_score += static_cast<int>(part1_this_game.my_shape) + static_cast<int>(part1_this_game.outcome);

        part2_this_game.my_shape = get_my_shape(part2_this_game.opponent_shape, part2_this_game.outcome);
        part2_score += static_cast<int>(part2_this_game.my_shape) + static_cast<int>(part2_this_game.outcome);
    }

    ifs.close();

    cout << "Part 1: " << part1_score << endl;
    cout << "Part 2: " << part2_score << endl;

    return 0;
}

GameOutcome get_outcome(GameShape player_shape, GameShape opponent_shape) {
    if (player_shape == opponent_shape) {
        return GameOutcome::Draw;
    } else if ((player_shape == GameShape::Paper && opponent_shape == GameShape::Rock) ||
                (player_shape == GameShape::Scissors && opponent_shape == GameShape::Paper) ||
                (player_shape == GameShape::Rock && opponent_shape == GameShape::Scissors)) {
        return GameOutcome::Win;
    } else {
        return GameOutcome::Lose;
    }
}

GameShape get_my_shape(GameShape opponent_shape, GameOutcome outcome) {
    if (outcome == GameOutcome::Draw) {
        return opponent_shape;
    } else if (outcome == GameOutcome::Win) {
        switch (opponent_shape) {
            case GameShape::Paper:
                return GameShape::Scissors;
            case GameShape::Rock:
                return GameShape::Paper;
            case GameShape::Scissors:
                return GameShape::Rock;
        }
    } else {
        switch (opponent_shape) {
            case GameShape::Paper:
                return GameShape::Rock;
            case GameShape::Rock:
                return GameShape::Scissors;
            case GameShape::Scissors:
                return GameShape::Paper;
        }
    }
}
