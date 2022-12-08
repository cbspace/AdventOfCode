#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

enum class ElementType {
    file,
    folder
};

struct DirElement
{
    ElementType type;
    string name;
    long int size; 
    vector<DirElement*> contents;
    DirElement* parent;
};

struct Computer 
{
    int memory {70000000};
    DirElement* root_directory {nullptr};
    DirElement* current_directory {nullptr};
    vector<int>* smallest {new vector<int>};
    vector<int>* largest {new vector<int>};
};

void process_instruction(string const&, Computer*);
void calculate_directory_sizes(vector<DirElement*> const&, int);
void print_directory_structure(vector<DirElement*> const&, int);
void get_small_dirs(vector<DirElement*> const&, vector<int>*, int);
void get_large_dirs(vector<DirElement*> const&, vector<int>*, int);

int main(int, char**) {
    fstream ifs;
    string line_str;

    DirElement root_folder = { ElementType::folder, "/", 0, {*new vector<DirElement*>}, nullptr };
    vector<DirElement*> root_container = {&root_folder};

    Computer* my_computer = new Computer;
    my_computer->root_directory = &root_folder;

    ifs.open("input/day7_input.txt", ios::in);

    while (!ifs.eof()) {
        getline(ifs, line_str);

        if (line_str.empty())
            break;

        process_instruction(line_str, my_computer);
    }
    ifs.close();


    calculate_directory_sizes(root_container, 0);
    print_directory_structure(root_container, 0);

    get_small_dirs(root_container, my_computer->smallest, 100000);
    int total = 0;
    for (int d : *my_computer->smallest) {
        total += d;
    }
    cout << "Part 1: " << total << endl;

    int space_required = 30000000 - (my_computer->memory - my_computer->root_directory->size);
    get_large_dirs(root_container, my_computer->largest, space_required);
    int lowest = my_computer->memory;
    for (int d : *my_computer->largest) {
        if (d < lowest)
            lowest = d;
    }
    cout << "Part 2: " << lowest << endl;

    return 0;
}

void process_instruction(string const& instruction, Computer* c) {
    if (instruction[0] == '$') {
        if (instruction.substr(2,2) == "cd") {
            string new_dir = instruction.substr(5);
            if (new_dir == "/") {
                c->current_directory = c->root_directory;
            } else if (new_dir == "..") {
                c->current_directory = c->current_directory->parent;
            }    
            else {
                for (DirElement* d : c->current_directory->contents) {
                    if (d->name == new_dir) {
                        c->current_directory = d;
                        break;
                    }
                }
            }
        }
    } else {
        if (instruction.substr(0,3) == "dir") {
            DirElement* my_new_folder = new DirElement{ElementType::folder, instruction.substr(4), 0, {}, c->current_directory };
            c->current_directory->contents.push_back(my_new_folder);
        } else {
            int space_index = instruction.find(" ");
            long int s = stoi(instruction.substr(0,space_index));
            string n = instruction.substr(space_index+1);
            DirElement* my_new_file = new DirElement{ElementType::file, n, s, {}, c->current_directory };
            c->current_directory->contents.push_back(my_new_file);
        }
    }
}

void calculate_directory_sizes(vector<DirElement*> const& directory, int total_size) {
    for (DirElement* const d : directory) {
        if (!d->contents.empty()) {
            calculate_directory_sizes(d->contents, total_size);
        } else {
            DirElement* new_path = d;
            while (true) {
                if (new_path->parent == nullptr)
                    break;
                
                new_path->parent->size += d->size;
                new_path = new_path->parent;
            }
        }
    }
}

void get_small_dirs(vector<DirElement*> const& directory, vector<int>* small_list, int find_lower_or_eq) {
    for (DirElement* const d : directory) {
        int additional_total_size = 0;
        if ((d->type == ElementType::folder) && (d->size <= find_lower_or_eq)) {
            small_list->push_back(d->size);
        }

        if (!d->contents.empty()) {
            get_small_dirs(d->contents, small_list, find_lower_or_eq);
        }
    }
}

void get_large_dirs(vector<DirElement*> const& directory, vector<int>* small_list, int find_greater_or_eq) {
    for (DirElement* const d : directory) {
        int additional_total_size = 0;
        if ((d->type == ElementType::folder) && (d->size >= find_greater_or_eq)) {
            small_list->push_back(d->size);
        }

        if (!d->contents.empty()) {
            get_large_dirs(d->contents, small_list, find_greater_or_eq);
        }
    }
}

void print_directory_structure(vector<DirElement*> const& directory, int depth) {
    for (DirElement* const d : directory) {
        cout << setw(depth*2) << " " << "- " << d->name << " ";
        if (d->type == ElementType::folder) {
            cout << "(dir) size=" << d->size << ")" << endl;
        }
        else {
            cout << "(file, size=" << d->size << ")" << endl;
        }

        if (!d->contents.empty()) {
            print_directory_structure(d->contents, depth + 1);
        }
    }
}