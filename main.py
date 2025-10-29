from c4.board import create_board, column_is_full, drop_disc, render
from c4.rules import in_bounds, balanced_test, vertical_test

board = create_board()

print(drop_disc(board, 1, "o"))
print(drop_disc(board, 2, "x"))
print(drop_disc(board, 2, "o"))
print(drop_disc(board, 3, "x"))
print(drop_disc(board, 3, "x"))
print(drop_disc(board, 3, "o"))
print(drop_disc(board, 4, "x"))
print(drop_disc(board, 4, "x"))
print(drop_disc(board, 4, "x"))
print(drop_disc(board, 4, "o"))


render(board)
print(in_bounds(board, 6))
print(balanced_test(board, 6, "o"))
print(vertical_test(board, 2, "o"))


