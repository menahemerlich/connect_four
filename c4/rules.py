
def in_bounds(board: list[list[str]], col: int) -> bool:
    if col > len(board[0]):
        return False
    return True

def balanced_test(board: list[list[str]], row: int, mark: str) -> bool:
    test = ""
    mark_test = mark * 4
    for i in range(len(board[0])):
        test += board[row][i]
    if mark_test in test:
        return True
    return False

def vertical_test(board: list[list[str]], col: int, mark: str) -> bool:
    test = ""
    mark_test = mark * 4
    for i in range(len(board)):
        test += board[i][col]
    if mark_test in test:
        return True
    return False

def diagonal_test(board: list[list[str]], row: int, col: int, mark: str)
    pass





