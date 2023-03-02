#!/usr/bin/python3
'''
Solution module for island perimeter
'''


def island_perimeter(grid):
    '''
    A function which calculats and return the perimeter
    of island in given grid
    '''
    width = len(grid[0])
    height = len(grid)
    perimeter = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
