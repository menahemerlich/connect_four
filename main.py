from c4.board import create_board, column_is_full, drop_disc, render
from c4.rules import in_bounds

board = create_board()

print(render(board))
print(drop_disc(board, 2, "o"))

print(drop_disc(board, 2, "x"))

for i in board:
    for j in i:
        print(j, end=" ")
    print()
print(in_bounds(board, 6))


