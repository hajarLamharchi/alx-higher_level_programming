#!/usr/bin/python3
"""This function finds the peak of an insorted list of integers"""


def find_peak(list_of_integers):
    """This function finds the peak of an insorted list of integers"""
    n = len(list_of_integers)
    left = 0
    right = n - 1

    while left <= right:
        m = (left + right) // 2
        if ((m == 0 or list_of_integers[m - 1] <= list_of_integers[m]) and
           (m == n - 1 or list_of_integers[m] >= list_of_integers[m + 1])):
            return list_of_integers[m]

        if m == 0 or list_of_integers[m - 1] > list_of_integers[m]:
            right = m - 1
        else:
            left = m + 1
