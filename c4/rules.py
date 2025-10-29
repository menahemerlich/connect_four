
def in_bounds(board: list[list[str]], col: int) -> bool:
    if col > len(board[0]):
        return False
    return True