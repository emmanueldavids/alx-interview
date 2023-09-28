#!/usr/bin/python3


""" Creating a function called def island_perimeter(grid):
    to return the perimeter of the island described in grid
    grid is a list of list of integers: 
    0 represents water, 1 represents land
"""


def island_perimeter(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides for each land cell

                # Check the adjacent cells (top, bottom, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
