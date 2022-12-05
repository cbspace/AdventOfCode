#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

void fill_stacks(vector<string> const&, vector<stack<string>> &);
void process_move(string const&, vector<stack<string>> & stacks, bool);

int main(int, char**) {
    fstream ifs;
    string line_str;
    vector<string> initial_stack;
    int no_of_stacks;
    vector<stack<string>> part1_stacks, part2_stacks;

    ifs.open("input/day5_input.txt", ios::in);

    while (true) {
        getline(ifs, line_str);
        if (line_str.substr(0,2) == " 1")
            break;
        initial_stack.insert(initial_stack.begin(),line_str);
    }

    no_of_stacks = (line_str.length() + 1) / 4;
    for (int i = 0; i < no_of_stacks; i++) {
        part1_stacks.push_back(*new stack<string>);
        part2_stacks.push_back(*new stack<string>);
    }

    fill_stacks(initial_stack, part1_stacks);
    fill_stacks(initial_stack, part2_stacks);
    getline(ifs, line_str);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        process_move(line_str, part1_stacks, false);
        process_move(line_str, part2_stacks, true);
    }
    ifs.close();

    cout << "Part 1: ";
    for (stack<string> & s : part1_stacks) {
        if (!s.empty())
            cout << s.top();
    }
    cout << endl;

    cout << "Part 2: ";
    for (stack<string> & s : part2_stacks) {
        if (!s.empty())
            cout << s.top();
    }
    cout << endl;

    return 0;
}

void fill_stacks(vector<string> const& initial_stack, vector<stack<string>> & stacks) {
    for (string const& s : initial_stack) {
        for (int stack_no = 0; stack_no < stacks.size(); stack_no++) {
            int stack_position = stack_no * 4 + 1;
            string stack_element = s.substr(stack_position,1);
            if (stack_element != " ") {
                stacks[stack_no].push(stack_element);
            }
        }
    }
}

void process_move(string const& instruction, vector<stack<string>> & stacks, bool keep_order) {
    int move_amount, from_move, to_move;
    if (instruction.substr(6,1) == " ") {
        move_amount = stoi(instruction.substr(5,1));
        from_move = stoi(instruction.substr(12,1)) - 1;
        to_move = stoi(instruction.substr(17,1)) - 1;
    } else {
        move_amount = stoi(instruction.substr(5,2));
        from_move = stoi(instruction.substr(13,1)) - 1;
        to_move = stoi(instruction.substr(18,1)) - 1;
    }

    if (keep_order) {
        stack<string> temp_stack = stacks[from_move];
        for (int i = 0; i < move_amount; i++) {
            temp_stack.push(stacks[from_move].top());
            stacks[from_move].pop();
        }

        for (int i = 0; i < move_amount; i++) {
            stacks[to_move].push(temp_stack.top());
            temp_stack.pop();
        }
    } else {
        for (int i = 0; i < move_amount; i++) {
            stacks[to_move].push(stacks[from_move].top());
            stacks[from_move].pop();
        }
    }


}