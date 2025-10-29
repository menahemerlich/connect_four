
def create_board(rows: int = 7, cols: int = 6) -> list[list[str]]:
    board = []
    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append("_")
    return board

def column_is_full(board: list[list[str]], col: int) -> bool:
    for i in range(len(board)):
        if board[i][col] == "_":
            return False
    return True

def drop_disc(board: list[list[str]], col: int, mark: str) -> tuple[int, int] | None:
    depth = len(board)
    if not column_is_full(board, col):
        for i in range(depth):
            if board[depth - 1 - i][col] == "_":
                board[depth - 1 - i][col] = mark
                return i, col
    return None






