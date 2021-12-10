filename = 'input.txt'

with open(filename) as f:
    nums = [int(x) for x in f.readline().split(',')]
    f.readline()

    boards = []
    board_buffer = []
    for line in f:
        row = [int(x) for x in line.split()]
        if len(row) != 0:
            board_buffer.append(row)
        else:
            boards.append(board_buffer)
            board_buffer = []

    if len(board_buffer) != 0:
        boards.append(board_buffer)
        board_buffer = []
f.close()

num_boards = len(boards)
num_rows = len(boards[0])
num_cols = len(boards[0][0])

score_boards = [[[0 for x in range(num_cols)] for y in range(num_rows)] for z in range(num_boards)]

winning_board = None
winning_num = None
for num in nums:
    if winning_num != None:
        break

    for i, board in enumerate(boards):
        if winning_num != None:
            break

        coordinates = [(x, y) for x, row in enumerate(board) for y, value in enumerate(row) if value == num]
        for row, col in coordinates:
            score_boards[i][row][col] += 1
            row_score = sum(score_boards[i][row])
            col_score = [sum(x) for c, x in enumerate(zip(*score_boards[i])) if c == col][0]
            if row_score == num_rows or col_score == num_cols:
                winning_board = i
                winning_num = num
                break

sum_of_unmarked = 0
for x in range(num_rows):
    for y in range(num_cols):
        if score_boards[winning_board][x][y] != 1:
            sum_of_unmarked += boards[winning_board][x][y]

print(sum_of_unmarked*winning_num)