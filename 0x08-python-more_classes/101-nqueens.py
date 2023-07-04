#!/usr/bin/python3
import sys

import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False
    return True


def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0


def print_solution(board):
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


if len(sys.argv) != 2:
    print("Usage: ./101-nqueens.py N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for _ in range(N)] for _ in range(N)]

solve_nqueens(board, 0)
