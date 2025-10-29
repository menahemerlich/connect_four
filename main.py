from c4.board import create_board, column_is_full, drop_disc

board = create_board()

for i in board:
    for j in i:
        print(j, end=" ")
    print()
print(drop_disc(board, 2, "o"))
for i in board:
    for j in i:
        print(j, end=" ")
    print()
print(drop_disc(board, 2, "x"))

for i in board:
    for j in i:
        print(j, end=" ")
    print()


