import sys

# Polymer template
p_template = []

# Polymer rules
p_rules_l = []
p_rules_r = []

# Open file and populate template and rules
infile = open("Day14_input.txt","r")
line_data = infile.readline()
line_data = line_data.strip()
for a in line_data.strip():
    p_template.append(a)
infile.readline()

for l in infile:
    line_data = l.strip()
    line_array = line_data.split(' -> ')
    p_rules_l.append(line_array[0])
    p_rules_r.append(line_array[1])

# Create deep copy of array
def array_deep_copy(array_in):
    new_array = []
    for i in array_in:
        new_array.append(i)
    return new_array

# Function to match rule
def match_rule(in_sequence):
    for rule in p_rules_l:
        if rule == in_sequence:
            return p_rules_r[p_rules_l.index(in_sequence)]
    return ""

# Function to do a single step
def do_step():
    global p_template
    new_template = []

    for e in range(len(p_template)-1):
        new_template.append(p_template[e])
        matched = match_rule(p_template[e] + p_template[e+1])
        if matched != "":
            new_template.append(matched)
    new_template.append(p_template[-1])
    p_template = array_deep_copy(new_template)

# Loop through steps
for i in range(10):
    do_step()

total_counts = []
characters = list(dict.fromkeys(p_rules_r))
for c in characters:
    total_counts.append(p_template.count(c))

total_counts.sort()
print(total_counts[-1] - total_counts[0])