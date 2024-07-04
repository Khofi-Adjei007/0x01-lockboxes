#!/usr/bin/python3
"""
Module to solve the N-Queens problem.
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursive backtracking function to find all solutions for the N-Queens problem.

    Args:
        r (int): The current row being processed.
        n (int): The total number of queens (and the size of the board).
        cols (set): Set of columns where queens are placed.
        pos (set): Set of positive diagonals where queens are placed.
        neg (set): Set of negative diagonals where queens are placed.
        board (list): 2D list representing the chessboard with queens placed.

    Returns:
        None
    """
    if r == n:
        result = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    result.append([row, col])
        print(result)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r + 1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solves the N-Queens problem for a given size n.

    Args:
        n (int): Number of queens (and the size of the
        chessboard). Must be >= 4.

    Returns:
        None
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(args[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
