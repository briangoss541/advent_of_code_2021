from collections import defaultdict

sample_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

# in_data = sample_input.split('\n')

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

pulled_numbers = [int(x) for x in in_data[0].split(',')]

# Data to boards
board_data = dict()
board_num = 0
start_window = 0

del(in_data[0:2])

for end_window in range(5, len(in_data), 6):

    board_data[board_num] = list()

    for value_list in in_data[start_window:end_window]:
        row_list = [int(x) for x in value_list.split(' ') if len(x) > 0]

        if len(row_list) > 0:
            board_data[board_num].append(row_list)

    start_window = end_window

    board_num += 1

# Create version for marking
hits_dict = {k: list() for k in board_data}

# Create diagonal templates
diag_1 = set()
diag_2 = set()
for z in range(5):
    diag_1.add((z, z))
    diag_2.add((4 - z, z))

# Go through pulled numbers and mark boards
winning_number = None
winning_boards = set()
total_boards = set(board_data)
last_board = None
for pulled_number in pulled_numbers:

    print(f'Pulling number {pulled_number}')

    for target_board in board_data:

        for x_value, target_row in enumerate(board_data[target_board]):
            for y_value, target_value in enumerate(target_row):

                if target_value == pulled_number:
                    hits_dict[target_board].append((x_value, y_value))

    # Check those boards
    for target_board in hits_dict:

        if target_board in winning_boards:
            continue

        # Diagonals
        # if len(diag_1 - set(hits_dict[target_board])) == 0 or len(diag_2 - set(hits_dict[target_board])) == 0:
        #     winning_number = pulled_number
        #     winning_board = target_board

        # Rows, columns
        x_counter = defaultdict(int)
        y_counter = defaultdict(int)
        for x_value, y_value in hits_dict[target_board]:
            x_counter[x_value] += 1
            y_counter[y_value] += 1

        for x_value, x_count in x_counter.items():
            if x_count == 5:
                winning_boards.add(target_board)
                winning_number = pulled_number
                last_board = target_board
        for y_value, y_count in y_counter.items():
            if y_count == 5:
                winning_boards.add(target_board)
                winning_number = pulled_number
                last_board = target_board

    if len(total_boards - winning_boards) == 0:
        break

print(f'Last board: {last_board}')

# Summing unmarked from last board
winning_board_sum = 0

for x_value, target_row in enumerate(board_data[last_board]):
    for y_value, target_col in enumerate(target_row):
        if (x_value, y_value) not in hits_dict[last_board]:
            winning_board_sum += target_col

print(f'Sum is {winning_board_sum} and winning number is {winning_number}')
print(winning_board_sum * winning_number)
