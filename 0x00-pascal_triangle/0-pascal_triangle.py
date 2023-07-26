#!/usr/bin/python3
"""Pascal's Triangle module"""
# Uses a list of lists to create a pascal triangle of size n


def pascal_triangle(n):
    """Pascal's Triangle function"""
    if (n <= 0):
        return []
    else:
        # Initial row of the triangle
        pascal = [[1]]
        # Loop to create the triangle using the previous row
        for i in range(1, n):
            # Initial row of the triangle always starts with 1
            row = [1]
            # Loop to calculate the values of the current row
            for j in range(1, i):
                # Adds the sum of the successive two numbers above
                # the current position to the initial 1 in the row
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            # Final calculated row of the triangle always ends with 1
            row.append(1)
            # Adds the row to the triangle
            pascal.append(row)
        return pascal
