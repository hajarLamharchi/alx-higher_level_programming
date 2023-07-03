#!/usr/bin/python3
""" This module defines the N queens puzzle:
    it is the challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys


def nqueens(n):
    """ This function defines the nqueens puzzle
        Args:
        n(int): size of the chessboard
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_empty(board, row, col):
        """ Checks if the position is clear """
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtrack(board, col):
        if col >= n :
            for row in board:
                print(' '.join(row))
            print()

        for i in range(n):
            if is_empty(board, i, col):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'
