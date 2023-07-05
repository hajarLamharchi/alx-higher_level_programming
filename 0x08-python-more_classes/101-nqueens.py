#!/usr/bin/python3
""" This module defines the N queens puzzle:
    it is the challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

def NQueens(n):
    """ This function defines the N queens puzzle
        Arg:
        n (int): size of the chessboard always >= 4
    """
    n = int(sys.argv[1])
    if not isinstance(n, int):
        print('N must be a number')
        sys.exit(1)
    elif n < 4:
        print('N must be at least 4')
        sys.exit(1)

    col = set()
    pos_diag = set()
    neg_diag = set()

    result = []

    def backtrack(board, r):
        """ Defines bachtracking algorithm"""
        if r == n:
            new_board = [[i, board[i]] for i in range(n)]
            result.append(new_board)
            return
        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r] = c
            backtrack(board, r + 1)
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack([None] * n, 0)
    return result


solutions = NQueens(int(sys.argv[1]))
for s in solutions:
    print(s)
