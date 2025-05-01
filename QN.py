def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens(n, col=0, board=None, solutions=None):
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if col == n:
        solutions.append(board[:])
        print_board(board, n)
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens(n, col + 1, board, solutions)
            board[col] = -1  # backtrack

def print_board(board, n):
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(' '.join(row))
    print()

# Change n to any number >= 4
n = 6
solve_n_queens(n)
