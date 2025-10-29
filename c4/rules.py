
def in_bounds(board: list[list[str]], col: int) -> bool:
    if col > len(board[0]):
        return False
    return True

def balanced_test(board: list[list[str]], row: int, col: int) -> bool:
    test = ""
    mark = board[row][col]
    mark_test = mark * 4
    for i in range(len(board[0])):
        test += board[row][i]
    if mark_test in test:
        return True
    return False

def vertical_test(board: list[list[str]], row: int, col: int) -> bool:
    test = ""
    mark = board[row][col]
    mark_test = mark * 4
    for i in range(len(board)):
        test += board[i][col]
    if mark_test in test:
        return True
    return False

def diagonal_test_1(board: list[list[str]], row: int, col: int) -> bool:
    test = ""
    mark = board[row][col]
    mark_test = mark * 4
    while 0 <= col < len(board[0]) and 0 <= row < len(board) - 1:
        col -= 1
        row += 1
    while 0 <= col < len(board[0]) and 0 <= row < len(board):
        test += board[row][col]
        row -= 1
        col += 1
    if mark_test in test:
        return True
    return False

def diagonal_test_2(board: list[list[str]], row: int, col: int) -> bool:
    test = ""
    mark = board[row][col]
    mark_test = mark * 4
    while 0 < col < len(board[0]) and 0 <= row < len(board):
        col -= 1
        row -= 1
    while 0 <= col < len(board[0]) and 0 <= row < len(board):
        test += board[row][col]
        row += 1
        col += 1
    if mark_test in test:
        return True
    return False






