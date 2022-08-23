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
            return p_rules_l.index(in_sequence)
    return -1

# Total counts for each pair
pair_counts = []
for p in p_rules_l:
    pair_counts.append(0)
for i in range(len(p_template)-1):
    matched = match_rule(p_template[i] + p_template[i+1])
    if matched != -1:
        pair_counts[matched] += 1

# Calculate character counts
total_counts = []
characters = list(dict.fromkeys(p_rules_r))
for c in characters:
    total_counts.append(p_template.count(c))

# Function to do a single step
def do_step():
    global pair_counts
    global total_counts

    # Total counts for each pair
    pair_counts_new = array_deep_copy(pair_counts)

    for i in range(len(pair_counts)):
        if pair_counts[i] > 0:
            pair_counts_new[i] -= pair_counts[i]
            matched = match_rule(p_rules_l[i])
            new_sequence1 = p_rules_l[i][0] + p_rules_r[matched]
            new_sequence2 = p_rules_r[matched] + p_rules_l[i][1]
            pair_counts_new[p_rules_l.index(new_sequence1)] += pair_counts[i]
            pair_counts_new[p_rules_l.index(new_sequence2)] += pair_counts[i]
            total_counts[characters.index(p_rules_r[matched])] += pair_counts[i]

    pair_counts = array_deep_copy(pair_counts_new)

# Loop through steps
for i in range(40):
    do_step()

total_counts.sort()
print(total_counts[-1] - total_counts[0])