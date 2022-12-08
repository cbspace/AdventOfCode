#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool check_tree(vector<vector<int>> &, int, int);
int tree_view(vector<vector<int>> &, int, int);

int main(int, char**) {
    fstream ifs;
    string line_str;
    int visible_trees = 0;
    auto trees = vector<vector<int>>();
    auto visible = vector<vector<int>>();
    auto scenic_score = vector<int>();

    ifs.open("input/day8_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        auto tree_line = vector<int>();
        for (const char c : line_str) {
            tree_line.push_back(c - '0');
        }
        trees.push_back(tree_line);
    }
    ifs.close();

    for (int y = 0; y < trees.size(); y++) {
        vector<int> row = trees[y];
        for (int x = 0; x < trees[0].size(); x++) {
            visible_trees += check_tree(trees, y, x);
            scenic_score.push_back(tree_view(trees, y, x));
        }
    }

    cout << "Part 1: " << visible_trees << endl;

    int max_score = 0;
    for (int s : scenic_score) {
        if (s > max_score)
            max_score = s;
    }
    cout << "Part 2: " << max_score << endl;

    return 0;
}

int tree_view(vector<vector<int>> & trees, int tree_y, int tree_x) {
    int y_max = trees.size() - 1;
    int x_max = trees[0].size() - 1;
    int view_left = 0;
    int view_right = 0;
    int view_top = 0;
    int view_bottom = 0;

    if (tree_x > 0) {
        for (int x = tree_x; x >= 1; x--) {
            if (trees[tree_y][tree_x] > trees[tree_y][x - 1]) 
                view_left++;
            else {
                view_left++;
                break;
            }
        }
    }

    if (tree_x < x_max) {
        for (int x = tree_x; x <= x_max - 1; x++) {
            if (trees[tree_y][tree_x] > trees[tree_y][x + 1])
                view_right++;
            else {
                view_right++;
                break;
            }
        }
    }

    if (tree_y > 0) {
        for (int y = tree_y; y >= 1; y--) {
            if (trees[tree_y][tree_x] > trees[y - 1][tree_x])
                view_top++;
            else {
                view_top++;
                break;
            }
        }
    }

    if (tree_y < y_max) {
        for (int y = tree_y; y <= y_max - 1; y++) {
            if (trees[tree_y][tree_x] > trees[y + 1][tree_x])
                view_bottom++;
            else {
                view_bottom++;
                break;
            }
        }
    }
    
    return view_left * view_right * view_top * view_bottom;
}

bool check_tree(vector<vector<int>> & trees, int tree_y, int tree_x) {
    int y_max = trees.size() - 1;
    int x_max = trees[0].size() - 1;

    if ((tree_y * tree_x == 0) || (tree_y == y_max) || tree_x == x_max) {
        return true;
    }

    auto visible_left = [&] {
        for (int x = tree_x; x >= 1; x--) {
            if (trees[tree_y][tree_x] <= trees[tree_y][x - 1])
                return false;
        }
        return true;
    };
    auto visible_right = [&] {
        for (int x = tree_x; x <= x_max - 1; x++) {
            if (trees[tree_y][tree_x] <= trees[tree_y][x + 1])
                return false;
        }
        return true;
    };
    auto visible_top = [&] {
        for (int y = tree_y; y >= 1; y--) {
            if (trees[tree_y][tree_x] <= trees[y - 1][tree_x])
                return false;
        }
        return true;
    };
    auto visible_bottom = [&] {
        for (int y = tree_y; y <= y_max - 1; y++) {
            if (trees[tree_y][tree_x] <= trees[y + 1][tree_x])
                return false;
        }
        return true;
    };

    return visible_left() || visible_right() || visible_top() || visible_bottom();
}