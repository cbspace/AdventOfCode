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
void print_grid(vector<GridPoint> const&);

int main(int, char**) {
    fstream ifs;
    string line_str;
    vector<GridPoint> knots;

    for (int i = 0; i <=9; i++)
        knots.push_back(GridPoint());

    vector<GridPoint> tail_visited;
    tail_visited.push_back(knots[knots.size()-1]);

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
            knots[0].x += x_move;
            knots[0].y += y_move;
            for (int k = 1; k <= knots.size()-1; k++) {
                move_knot(knots, k-1, k, tail_visited);
            }
            print_grid(knots);
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

void print_grid(vector<GridPoint> const& knots) {
    for (int y = 4; y >= 0; y--) {
        for (int x = 0; x <= 5; x++) {
            GridPoint p = GridPoint {x,y};
            if (p == knots[0]) {
                cout << "H";
            } else if (p == knots[1]) {
                cout << "1";
            } else if (p == knots[2]) {
                cout << "2";
            } else if (p == knots[3]) {
                cout << "3";
            } else if (p == knots[4]) {
                cout << "4";
            } else if (p == knots[5]) {
                cout << "5";
            } else if (p == knots[6]) {
                cout << "6";
            } else if (p == knots[7]) {
                cout << "7";
            } else if (p == knots[8]) {
                cout << "8";
            } else if (p == knots[9]) {
                cout << "9";
            } else {
                cout << ".";
            }        
        }
        cout << endl;
    }
    cout << endl;
}