#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        temp_list = list(tuple_b)
        temp_list = [0, 0]
        tuple_b = tuple(temp_list)
    elif len(tuple_b) == 1:
        temp_list = list(tuple_b)
        temp_list.append(0)
        tuple_b = tuple(temp_list)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
