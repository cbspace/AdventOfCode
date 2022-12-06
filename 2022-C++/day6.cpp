#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool test_unique(string const &);

int main(int, char**) {
    fstream ifs;
    string line_str;

    ifs.open("input/day6_input.txt", ios::in);
    getline(ifs, line_str);
    ifs.close();

    for (int i = 0; i < line_str.length() - 4; i++) {
        string test_str = line_str.substr(i,4);
        if (test_unique(test_str)) {
            cout << "Part 1: " << i + 4 << endl;
            break;
        }
    }

    for (int i = 0; i < line_str.length() - 14; i++) {
        string test_str = line_str.substr(i,14);
        if (test_unique(test_str)) {
            cout << "Part 2: " << i + 14 << endl;
            break;
        }
    }

    return 0;
}

bool test_unique(string const & test_str) {
    string chars;
    for (const char c : test_str) {
        if (chars.find(c) != std::string::npos)
            return false;
        chars += c;
    }
    return true;
}