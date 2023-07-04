#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if it's safe to place a queen at position (row, col)
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check for queens in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # It's safe to place a queen at position (row, col)
    return True


def solve_nqueens(board, row):
    # Base case: all queens have been placed
    if row == N:
        print_solution(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Place the queen
            solve_nqueens(board, row + 1)  # Recur for the next row
            board[row][col] = '.'  # Backtrack and remove the queen


def print_solution(board):
    # Print the board configuration
    for row in board:
        print(' '.join(row))
    print()


# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [['.' for _ in range(N)] for _ in range(N)]

# Solve the N queens problem
solve_nqueens(board, 0)
