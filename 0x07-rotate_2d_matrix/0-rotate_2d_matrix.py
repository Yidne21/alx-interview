#!/usr/bin/python3
'''Rotate 2D MATRIX MODULE
'''


def rotate_2d_matrix(matrix):
    '''An algorithm which rotates
        2D Matrix
    '''
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
