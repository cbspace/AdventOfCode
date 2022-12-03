#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int part1(string const&);
int part2();

int main(int, char**) {
    fstream ifs;
    string line_str;

    int part1_total = 0;
    int part2_total = 0;
    vector<char> matching;

    ifs.open("input/day3_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;
            
        part1_total += part1(line_str);
    }

    ifs.close();

    cout << "Part 1: " << part1_total << endl;

    return 0;
}

int part1(string const& line_str) {
    int sack_size = line_str.length() / 2;
    string sack1_contents = line_str.substr(0,sack_size);
    string sack2_contents = line_str.substr(sack_size,line_str.length());
    int score;

    for (const char i : sack1_contents) {
        if (sack2_contents.find(i) != std::string::npos) {
            if (islower(i)) {
                score = i - 'a' + 1;
            } else {
                score = i - 'A' + 27;
            }
            break;
        }
    }
    return score;
}