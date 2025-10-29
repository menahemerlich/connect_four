from c4.board import create_board, column_is_full, drop_disc, render
from c4.rules import in_bounds, has_winner_from

board = create_board()
(drop_disc(board, 2, "x"))
(drop_disc(board, 2, "o"))
(drop_disc(board, 3, "x"))
(drop_disc(board, 3, "x"))
(drop_disc(board, 3, "o"))
(drop_disc(board, 4, "x"))
(drop_disc(board, 4, "x"))
(drop_disc(board, 4, "x"))
(drop_disc(board, 4, "o"))
(drop_disc(board, 5, "x"))
(drop_disc(board, 5, "x"))
(drop_disc(board, 5, "x"))
(drop_disc(board, 5, "x"))
(drop_disc(board, 5, "o"))


render(board)
print(in_bounds(board, 6))
# print(balanced_test(board, 6, ))
# print(vertical_test(board, 2, ))
print(has_winner_from(board, 5, 2))

