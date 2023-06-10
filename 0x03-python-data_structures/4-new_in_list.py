#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    i = 0
    for elm in my_list:
        if i == idx:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
        i += 1
    return my_list.copy()
