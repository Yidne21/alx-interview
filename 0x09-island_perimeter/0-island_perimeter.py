#!/usr/bin/python3
'''
Solution module for island perimeter
'''
from typing import List


def island_perimeter(grid: List) -> int:
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
