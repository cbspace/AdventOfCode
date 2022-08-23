import sys

# Function to check slop and
# return number of trees
def check_slope(slope):
    # local variables
    x=0
    count=0

    # Loop through array
    for i in range(0,len(map_arr),slope[1]):
        map_line = map_arr[i]
        if map_line[x%len(map_line)]=='#':
            count+=1
        x+=slope[0]

    return count

# map
map_arr = []

# Input file
infile = open('Day3_input.txt', 'r')

# Load file to map
for line in infile:
    map_arr.append(line.strip())
infile.close()

# Array of slopes
slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]

# Find total count
total_count = check_slope(slopes[0])

for s in range(1,len(slopes)):
    total_count *= check_slope(slopes[s])

print('The answer is',total_count)
