#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_range(string const);
bool check_if_in_range(vector<int> const&, vector<int> const&);
bool check_if_some_overlap(vector<int> const&, vector<int> const&);

int main(int, char**) {
    fstream ifs;
    string line_str;
    int part1_total = 0;
    int part2_total = 0;

    ifs.open("input/day4_input.txt", ios::in);

    while (!ifs.eof()) {
        vector<int> elf1, elf2;
        string str1, str2;
        bool overlapping;

        getline(ifs, line_str);
        if (line_str.empty())
            break;

        int delimiter_pos = line_str.find(',');
        str1 = line_str.substr(0,delimiter_pos);
        str2 = line_str.substr(delimiter_pos+1);

        elf1 = get_range(line_str.substr(0,delimiter_pos));
        elf2 = get_range(line_str.substr(delimiter_pos+1));

        if (elf1.size() == elf2.size()) {
            overlapping = check_if_in_range(elf1, elf2);
        } else if (elf1.size() > elf2.size()) {
            overlapping = check_if_in_range(elf1, elf2);
        } else {
            overlapping = check_if_in_range(elf2, elf1);
        }

        if (overlapping)
            part1_total++;

        if (check_if_some_overlap(elf1, elf2))
            part2_total++;
    }

    ifs.close();

    cout << "Part 1: " << part1_total << endl;
    cout << "Part 2: " << part2_total << endl;

    return 0;
}

vector<int> get_range(string const str_in) {
    vector<int> elf_range;
    int delimiter_pos = str_in.find('-');
    int start = stoi(str_in.substr(0,delimiter_pos));
    int end = stoi(str_in.substr(delimiter_pos+1));

    for (int i=start; i<=end; i++)
        elf_range.push_back(i);
    return elf_range;
}

bool check_if_in_range(vector<int> const& larger, vector<int> const& smaller) {
    for (const int i : smaller) {
        if (find(larger.begin(), larger.end(), i) == larger.end())
            return false;
    }
    return true;
}

bool check_if_some_overlap(vector<int> const& larger, vector<int> const& smaller) {
    for (const int i : smaller) {
        if (find(larger.begin(), larger.end(), i) != larger.end())
            return true;
    }
}