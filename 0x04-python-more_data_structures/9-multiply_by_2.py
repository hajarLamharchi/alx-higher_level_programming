#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = map(lambda x: x * 2, a_dictionary.values())
    new_dict = dict(zip(a_dictionary.keys(), values))
    return new_dict
