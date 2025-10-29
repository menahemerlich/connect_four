from c4.board import create_board

board = create_board()
for i in board:
    for j in i:
        print(j, end=" ")
    print()

