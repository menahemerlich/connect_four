from .test_winner import balanced_test, vertical_test, diagonal_test_1, diagonal_test_2

def in_bounds(board: list[list[str]], col: int) -> bool:
    if col > len(board[0]):
        return False
    return True

def has_winner_from(board: list[list[str]], row: int, col: int) -> bool:
    if balanced_test(board, row, col) or vertical_test(board, row, col) or diagonal_test_1(board, row, col) or diagonal_test_2(board, row, col):
        return True
    return False








