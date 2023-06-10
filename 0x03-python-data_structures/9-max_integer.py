#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    max_int = 0
    for element in my_list:
        if element > max_int:
            temp = element
            element = max_int
            max_int = temp
    return max_int
