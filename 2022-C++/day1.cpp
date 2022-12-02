#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main(int, char**) {

    fstream ifs;
    string line_str;
    vector<int> calories;

    ifs.open("input/day1_input.txt", ios::in);

    int calories_for_elf = 0;

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty()) {
            calories.push_back(calories_for_elf);
            calories_for_elf = 0;
        }
        else {
            calories_for_elf += stoi(line_str);
        }
    }

    ifs.close();

    sort(calories.begin(), calories.end());
    cout << "Part 1: " << calories.back() << endl;

    auto sum = accumulate(calories.end() -3, calories.end(), 0);    
    cout << "Part 2: " << sum << endl;

    return 0;
}