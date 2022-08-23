import sys

def check_win_hor(board,no_drawn):
    win = False
    marked_numbers = []
    for r in board:
        if win == False:
            winning_row = []
        for c in range(len(r)):
            for d in range(no_drawn):
                if r[c] == b_numbers[d]:
                    marked_numbers.append(b_numbers[d])
                    winning_row.append(b_numbers[d])
                    #print(winning_row)
                    if len(winning_row) == 5:
                        win = True

    if win == True:
        total_marked = 0
        #print(marked_numbers)
        for a in marked_numbers:
            total_marked += a
        return total_marked
    else:
        return 0

def check_win_ver(board,no_drawn):
    win = False
    marked_numbers = []
    for c in range(4):
        if win == False:
            winning_col = []
        for r in board:
            for d in range(no_drawn):
                if r[c] == b_numbers[d]:
                    marked_numbers.append(b_numbers[d])
                    winning_col.append(b_numbers[d])
                    #print(winning_col)
                    if len(winning_col) == 5:
                        win = True

    if win == True:
        total_marked = 0
        #print(winning_col)
        for a in marked_numbers:
            total_marked += a
        return total_marked
    else:
        return 0

# Input file
infile = open("Day4_input.txt", "r")

# Array to store entries from file
boards = []

board_status = []

# Numbers
b_numbers = [int(i) for i in infile.readline().split(',')]

# Read file entries into array
while True:
    line = infile.readline()
    if not line:
        break
    board=[]
    for x in range(5):
        line = infile.readline().strip()
        board_row = [int(i) for i in line.split()]
        board.append(board_row)
    boards.append(board)
    board_status.append(False)
infile.close()

win_found = 0
for n in range(len(b_numbers)):
    for current_board in boards:
        if win_found == 0:
            win_found = check_win_hor(current_board,n)
            if win_found == 0:
                win_found = check_win_ver(current_board,n)
            if win_found > 0:
                board_status[boards.index(current_board)] = True

                total=0
                for r in current_board:
                    for c in r:
                        total += c
                ans = (total-win_found)*b_numbers[n-1]

                print("The answer is",ans)
