#!/usr/bin/python3
"""BackTracking Algorithm to solve N-Queens problem module"""
import sys

# Size of the board
board = 0
# Possible solutions
solutions = []
# Position of the queens
pos = None


def queen_input():
    """Receives the user's input and validates it"""
    global board
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    try:
        board = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if board < 4:
        print("N must be at least 4")
        sys.exit(1)


def isSafe(row, col):
    """Check if a queen can be placed on board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if (pos[row][i]):
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if (pos[i][j]):
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, board, 1), range(col, -1, -1)):
        if (pos[i][j]):
            return False
    return True


def is_attacking():
    """Checks which positions are attacking each other
    on the board
    """
    if len(pos) == 0:
        return False
    for i in range(board):
        for j in range(board):
            if pos[i][j]:
                for k in range(board):
                    if k != j:
                        pos[i][k] = True
                    if k != i:
                        pos[k][j] = True
                for k in range(board):
                    if i + k < board and j + k < board:
                        pos[i + k][j + k] = True
                    if i - k >= 0 and j - k >= 0:
                        pos[i - k][j - k] = True
                    if i + k < board and j - k >= 0:
                        pos[i + k][j - k] = True
                    if i - k >= 0 and j + k < board:
                        pos[i - k][j + k] = True
    return True

def solution_exists():
    """Checks whether a group of solutions exists"""
    global pos
    pos = [[False for j in range(board)] for i in range(board)]
    for i in range(board):
        for j in range(board):
            if isSafe(i, j):
                pos[i][j] = True
                if is_attacking():
                    return True
                pos[i][j] = False
    return False

def build_solutions():
    """Creates solutions for the input given by the user"""
    global solutions
    global board
    global pos
    pos = [[False for j in range(board)] for i in range(board)]
    for i in range(board):
        for j in range(board):
            if isSafe(i, j):
                pos[i][j] = True
                if is_attacking():
                    solutions.append(pos)
                pos[i][j] = False
    return solutions

def print_solutions():
    """Prints the solutions to the N-Queens problem"""
    global solutions
    global board
    if len(solutions) == 0:
        print("No solution")
        return
    for solution in solutions:
        for i in range(board):
            for j in range(board):
                if solution[i][j]:
                    print("[{:d}, {:d}]".format(i, j), end="")
        print("")
        
board = queen_input()
solution_exists()
build_solutions()
print_solutions()
for solution in solutions:
    print(solution)
