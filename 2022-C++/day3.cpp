#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int part1(string const&);
int part2(vector<string>&);

int main(int, char**) {
    fstream ifs;
    string line_str;

    int part1_total = 0;
    int part2_total = 0;
    int group_counter = 2;
    vector<string> group_of_3;

    ifs.open("input/day3_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;
            
        part1_total += part1(line_str);

        group_of_3.push_back(line_str);
        if (!group_counter) {
            part2_total += part2(group_of_3);
            group_of_3.clear();
            group_counter = 2;
        } else {
            group_counter--;
        }
    }
    ifs.close();

    cout << "Part 1: " << part1_total << endl;
    cout << "Part 2: " << part2_total << endl;

    return 0;
}

int part1(string const& line_str) {
    int sack_size = line_str.length() / 2;
    string sack1_contents = line_str.substr(0,sack_size);
    string sack2_contents = line_str.substr(sack_size,line_str.length());

    for (const char i : sack1_contents) {
        if (sack2_contents.find(i) != std::string::npos) {
            if (islower(i)) {
                return i - 'a' + 1;
            } else {
                return i - 'A' + 27;
            }
            break;
        }
    }
}

int part2(vector<string>& sacks) {
    for (const char i : sacks[0]) {
        if (sacks[1].find(i) != std::string::npos) {
            if (sacks[2].find(i) != std::string::npos) {
                if (islower(i)) {
                    return i - 'a' + 1;
                } else {
                    return i - 'A' + 27;
                }
            }
        }
    }
}