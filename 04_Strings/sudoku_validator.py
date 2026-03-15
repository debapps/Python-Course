"""A module to validate a completed Sudoku board."""

def valid_list(lst):
    """Check if a list contains all digits from 1 to 9 exactly once."""
    return sorted(lst) == list(range(1, 10))

def valid_rows(board):
    """Check if all rows in the Sudoku board are valid."""
    for row in board:
        if not valid_list(row):
            return False
    return True

def valid_columns(board):
    """Check if all columns in the Sudoku board are valid."""
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not valid_list(column):
            return False
    return True

def valid_subgrids(board):
    """Check if all 3x3 subgrids in the Sudoku board are valid."""
    for box_row in range(3):
        for box_col in range(3):
            subgrid = []
            for row in range(box_row * 3, box_row * 3 + 3):
                for col in range(box_col * 3, box_col * 3 + 3):
                    subgrid.append(board[row][col])
            if not valid_list(subgrid):
                return False
    return True

def is_valid_sudoku(board):
    """Check if the entire Sudoku board is valid."""
    return valid_rows(board) and valid_columns(board) and valid_subgrids(board)


if __name__ == "__main__":
    sudoku_board = '''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671'''
   
    board = [list(map(int, list(row))) for row in sudoku_board.split('\n')]
    print(is_valid_sudoku(board))



    