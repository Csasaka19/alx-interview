#!/usr/bin/python3
'''Minimum Operations module'''


def minOperations(n: int = 0) -> int:
    '''Minimum Operations function'''
    # Base case the operation is 0 if only 1 H
    if n <= 1:
        return 0
    else:
        # If n is even, the operation is 2 + minOperations(n / 2)
        for i in range(2, n + 1):
            # If n is odd, the operation is 1 + minOperations(n - 1)
            if n % i == 0:
                # recursive call
                return minOperations(int(n / i)) + i
