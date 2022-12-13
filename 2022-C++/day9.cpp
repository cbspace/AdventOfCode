#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct GridPoint
{
    int x {0};
    int y {0};
};

bool operator==(GridPoint const& lhs, GridPoint const& rhs){
    if ((lhs.x == rhs.x) && (lhs.y == rhs.y))
        return true;
    return false;
}

void move_knot(vector<GridPoint> &, int, int, vector<GridPoint> &);

int main(int, char**) {
    fstream ifs;
    string line_str;
    vector<GridPoint> knots1, knots2;

    for (int i = 0; i <= 1; i++)
        knots1.push_back(GridPoint());
    for (int i = 0; i <= 9; i++)
        knots2.push_back(GridPoint());

    vector<GridPoint> tail_visited1, tail_visited2;
    tail_visited1.push_back(knots1[0]);
    tail_visited2.push_back(knots2[9]);

    ifs.open("input/day9_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        char direction = line_str.at(0);
        int move_amount = stoi(line_str.substr(2));

        int x_move;
        int y_move;
        switch (direction)
        {
        case 'L':
            x_move = -1;
            y_move = 0;
            break;
        case 'R':
            x_move = 1;
            y_move = 0;
            break;
        case 'U':
            x_move = 0;
            y_move = 1;
            break;
        case 'D':
            x_move = 0;
            y_move = -1;
            break;
        }

        for (int i = 0; i < move_amount; i++) {
            knots1[0].x += x_move;
            knots1[0].y += y_move;
            move_knot(knots1, 0, 1, tail_visited1);
        }
        for (int i = 0; i < move_amount; i++) {
            knots2[0].x += x_move;
            knots2[0].y += y_move;
            for (int k = 1; k <= 9; k++) {
                move_knot(knots2, k-1, k, tail_visited2);
            }
        }

    }
    ifs.close();

    vector<GridPoint> unique1;
    for (GridPoint g : tail_visited1) {
        if (find(unique1.begin(), unique1.end(), g) == unique1.end())
            unique1.push_back(g);
    }
    vector<GridPoint> unique2;
    for (GridPoint g : tail_visited2) {
        if (find(unique2.begin(), unique2.end(), g) == unique2.end())
            unique2.push_back(g);
    }
    
    cout << "Part 1: " << unique1.size() << endl;
    cout << "Part 2: " << unique2.size() << endl;

    return 0;
}

void move_knot(vector<GridPoint> & knots, int head_index, int tail_index, vector<GridPoint> & tail_visited) {
    int delta_x = knots[head_index].x - knots[tail_index].x;
    int delta_y = knots[head_index].y - knots[tail_index].y;

    if (abs(delta_x) < 2 && abs(delta_y) < 2)
        return;
    
    if (abs(delta_y) == 2) {
        knots[tail_index].y += delta_y / 2;
        if (abs(delta_x) == 1)
            knots[tail_index].x += delta_x;
        if (abs(delta_x) == 2)
            knots[tail_index].x += delta_x / 2;
    } else if (abs(delta_x) == 2) {
        knots[tail_index].x += delta_x / 2;
        if (abs(delta_y) == 1)
            knots[tail_index].y += delta_y;
        if (abs(delta_y) == 2)
            knots[tail_index].y += delta_y / 2;
    }

    if (tail_index == knots.size()-1)
        tail_visited.push_back(knots[knots.size()-1]);

    return;
}