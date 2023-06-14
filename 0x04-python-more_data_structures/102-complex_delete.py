#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for k, v in a_dictionary.items():
        if v == value:
            delete.append(k)
    for key in delete:
        a_dictionary.pop(key)
    return a_dictionary
