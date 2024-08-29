#!/usr/bin/env python3
import sys

def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_nqueens(n, row=0, board=None):
    """
    Solves the N-Queens problem using backtracking.
    """
    if board is None:
        board = [-1] * n

    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)
            board[row] = -1

def main():
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)

if __name__ == "__main__":
    main()
