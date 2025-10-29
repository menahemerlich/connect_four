from c4.board import create_board, column_is_full

board = create_board()
for i in range(len(board)):
    board[i][2] = 'v'
for i in board:
    for j in i:
        print(j, end=" ")
    print()
print(column_is_full(board, 3))
