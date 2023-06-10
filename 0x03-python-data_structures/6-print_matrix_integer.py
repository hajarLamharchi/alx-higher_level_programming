#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    for i in range(len(matrix)):
        if not matrix[i]:
            print()
            continue
        for j in range(len(matrix[i]) - 1):
            print("{:d} ".format(matrix[i][j]), end="")
        print("{:d}".format(matrix[i][-1]))
