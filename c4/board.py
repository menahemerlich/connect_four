
def create_board(cols: int = 7, rows: int = 6) -> list[list[str]]:
    board = []
    for i in range(cols):
        board.append([])
        for j in range(rows):
            board[i].append("_")
    return board





