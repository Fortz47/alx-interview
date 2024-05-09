#!/usr/bin/python3
"""Island perimeter grid Module"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid:

     grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100

    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected
    to the water surrounding the island).
    """

    perimeter = 0
    grid_height = len(grid)
    grid_width = len(grid[0])

    for row in range(grid_height):
        for cell in range(grid_width):
            if grid[row][cell] != 1:
                continue
            right = 0 if grid[row][cell + 1] else 1
            left = 0 if grid[row][cell - 1] else 1
            up = 0 if grid[row - 1][cell] else 1
            down = 0 if grid[row + 1][cell] else 1
            perimeter += (right + left + up + down)
    return perimeter
