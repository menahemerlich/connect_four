from .test_winner import balanced_test, vertical_test, diagonal_test_1, diagonal_test_2

def in_bounds(board: list[list[str]], col: int) -> bool:
    if col > len(board[0]):
        return False
    return True

def has_winner_from(board: list[list[str]], row: int, col: int, mark:str) -> bool:
    if balanced_test(board, row, col, mark) or vertical_test(board, row, col, mark) or diagonal_test_1(board, row, col, mark) or diagonal_test_2(board, row, col, mark):
        return True
    return False

def has_winner(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if has_winner_from(board, i, j, "o"):
                return True
    return False

def is_full(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "_":
                return False
    return True





