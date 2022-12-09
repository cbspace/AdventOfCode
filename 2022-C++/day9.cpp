#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct GridPoint
{
    int x;
    int y;
};

bool operator==(const GridPoint& lhs, const GridPoint& rhs){
    if ((lhs.x == rhs.x) && (lhs.y == rhs.y))
        return true;
    return false;
}

void move_tail(GridPoint const&, GridPoint &, vector<GridPoint> &);

int main(int, char**) {
    fstream ifs;
    string line_str;

    GridPoint head_location {0, 0};
    GridPoint tail_location {0, 0};
    vector<GridPoint> tail_visited;
    tail_visited.push_back(tail_location);

    ifs.open("input/day9_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        char direction = line_str.at(0);
        int move_amount = stoi(line_str.substr(2));

        switch (direction)
        {
        case 'L':
            for (int i = 0; i < move_amount; i++) {
                head_location.x--;
                move_tail(head_location, tail_location, tail_visited);
            }
            break;
        case 'R':
            for (int i = 0; i < move_amount; i++) {
                head_location.x++;
                move_tail(head_location, tail_location, tail_visited);
            }
            break;
        case 'U':
            for (int i = 0; i < move_amount; i++) {
                head_location.y++;
                move_tail(head_location, tail_location, tail_visited);
            }
            break;
        case 'D':
            for (int i = 0; i < move_amount; i++) {
                head_location.y--;
                move_tail(head_location, tail_location, tail_visited);
            }
            break;
        }
    }
    ifs.close();

    vector<GridPoint> unique;
    for (GridPoint g : tail_visited) {
        if (find(unique.begin(), unique.end(), g) == unique.end())
            unique.push_back(g);
    }

    cout << "Part 1: " << unique.size() << endl;
    //cout << "Part 2: " << endl;

    return 0;
}

void move_tail(GridPoint const& head_location, GridPoint & tail_location, vector<GridPoint> & tail_visited) {
    int delta_x = head_location.x - tail_location.x;
    int delta_y = head_location.y - tail_location.y;

    if (abs(delta_x) < 2 && abs(delta_y) < 2)
        return;
    
    if (abs(delta_y) == 2) {
        tail_location.y += delta_y / 2;
        if (abs(delta_x) == 1)
            tail_location.x += delta_x;
    } else if (abs(delta_x) == 2) {
        tail_location.x += delta_x / 2;
        if (abs(delta_y) == 1)
            tail_location.y += delta_y;
    }

    tail_visited.push_back(tail_location);

    return;
}