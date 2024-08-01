#!/usr/bin/python3

"""Module to calculate the perimeter
    of an island in a grid."""


def island_perimeter(grid):

    """
    Calculate the perimeter of the island.
    The grid uses 0 to represent water and
    1 to represent land.
    Args:
        grid (list): A 2D list of integers
        representing the map.
    Returns:
        int: The perimeter of the island
        within the grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return size * 4 - edges * 2
