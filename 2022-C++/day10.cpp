#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Computer
{
    int cycle {0};
    int x_reg {1};
    int to_add_1 {0};
    int to_add_2 {0};
};

int main(int, char**) {
    fstream ifs;
    string line_str;
    Computer computer;
    vector<string> instructions;
    vector<int> const signals = {20, 60, 100, 140, 180, 220};
    int total = 0;

    ifs.open("input/day10_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        instructions.push_back(line_str);
        if (line_str != "noop")
            instructions.push_back("noop");
    }
    ifs.close();

    cout << "Part 2: " << endl;
    
    int index = 0;
    while (index < instructions.size()) {
        computer.x_reg += computer.to_add_1;
        computer.to_add_1 = computer.to_add_2;
        computer.cycle++;

        if (instructions[index].substr(0,4) == "addx") {
            int add_amount = stoi(instructions[index].substr(4));
            computer.to_add_2 = add_amount;
        } else {
            computer.to_add_2 = 0;
        }

        if (find(signals.begin(), signals.end(), computer.cycle) != signals.end())
            total += computer.cycle * computer.x_reg;

        int pixel_position = computer.cycle % 40 - 1;
        if ((pixel_position >= computer.x_reg - 1) && (pixel_position <= computer.x_reg + 1)) {
            cout << "#";
        } else {
            cout << ".";
        }
        if (computer.cycle % 40 == 0)
            cout << endl;

        index++;
    }

    cout << "Part 1: " << total << endl;

    return 0;
}