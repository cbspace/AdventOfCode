#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum class MonkeyOperator {
    plus,
    multiply
};

struct Monkey {
    vector<int> items;
    MonkeyOperator opearator;
    int operand; // -1 = "old"
    int test_amount;
    int throw_to_if_true;
    int throw_to_if_false;
};

int main(int, char**) {
    fstream ifs;
    string line_str;
    vector<Monkey> monkeys;
    Monkey new_monkey;

    ifs.open("input/day11_input1.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty()) {
            monkeys.push_back(new_monkey);
            new_monkey = Monkey();
            continue;
        }
        if (line_str.substr(0,6) == "Monkey")
            new_monkey = Monkey();
        if (line_str.substr(2,15) == "Starting items:") {
            string item_string = line_str.substr(18);
            for (int i = 0; i <= (item_string.length() - 2) / 4; i++) {
                new_monkey.items.push_back(stoi(item_string.substr(i*4,2)));
            }
        }
        if (line_str.substr(2,10) == "Operation:") {
            new_monkey.opearator = (line_str.substr(23,1) == "+") ? MonkeyOperator::plus : MonkeyOperator::multiply;
            if (line_str.substr(25) == "old")
                new_monkey.operand = -1;
            else
                new_monkey.operand = stoi(line_str.substr(25));
        }
        if (line_str.substr(2,5) == "Test:") {
            new_monkey.test_amount = stoi(line_str.substr(21));
        }
        if (line_str.substr(4,8) == "If true:") {
            new_monkey.throw_to_if_true = stoi(line_str.substr(29));
        }
        if (line_str.substr(4,9) == "If false:") {
            new_monkey.throw_to_if_false = stoi(line_str.substr(30));
        }
    }
    ifs.close();

    for (int round = 1; round <= 1; round++) {
        for (Monkey m : monkeys) {
            for (int item : m.items) {
                
            }
        }

    }

    cout << "Part 1: " << endl;
    cout << "Part 2: " << endl;

    return 0;
}