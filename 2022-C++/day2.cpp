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

GameOutcome get_outcome(GameShape, GameShape);
GameShape get_my_shape(GameShape, GameOutcome);

int main(int, char**) {
    fstream ifs;
    string line_str;
    int part1_score = 0;
    int part2_score = 0;

    ifs.open("input/day2_input.txt", ios::in);

    while (!ifs.eof()) {
        GameShape opponent_shape, part1_my_shape, part2_my_shape;
        GameOutcome part1_game_outcome, part2_game_outcome;

        getline(ifs, line_str);
        if (line_str.empty())
            break;

        switch (line_str[0]) {
            case 'A':
                opponent_shape = GameShape::Rock;
                break;
            case 'B':
                opponent_shape = GameShape::Paper;
                break;
            case 'C':
                opponent_shape = GameShape::Scissors;
                break;
        }

        switch (line_str[2]) {
            case 'X':
                part1_my_shape = GameShape::Rock;
                part2_game_outcome = GameOutcome::Lose;
                break;
            case 'Y':
                part1_my_shape = GameShape::Paper;
                part2_game_outcome = GameOutcome::Draw;
                break;
            case 'Z':
                part1_my_shape = GameShape::Scissors;
                part2_game_outcome = GameOutcome::Win;
                break;
        }

        part1_game_outcome = get_outcome(part1_my_shape, opponent_shape);
        part1_score += static_cast<int>(part1_my_shape) + static_cast<int>(part1_game_outcome);

        part2_my_shape = get_my_shape(opponent_shape, part2_game_outcome);
        part2_score += static_cast<int>(part2_my_shape) + static_cast<int>(part2_game_outcome);
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
