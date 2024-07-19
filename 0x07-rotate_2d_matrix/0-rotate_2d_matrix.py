#!/usr/bin/python3

"""Module for rotating a 2D matrix.
"""


def rotate_2d_matrix(matrix):

    """Rotates a square matrix 90
    degrees clockwise in place.

    Args:
        matrix (list of list of int):
        A square matrix to be rotated.
    """
    n = len(matrix[0])

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
