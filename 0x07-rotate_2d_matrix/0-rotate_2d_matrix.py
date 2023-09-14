#!/usr/bin/python3
""" Rotate 2D Matrix module"""


def rotate_2d_matrix(matrix) -> None:
    ''' Rotate 2D Matrix function'''
    if matrix is None:
        return None
    else:
        # This reverses the matrix which is the same as rotating it 90 degrees
        matrix.reverse()
        for i in range(len(matrix)):
            # This loop swaps the elements diagonally
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
