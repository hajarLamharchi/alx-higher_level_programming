#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for k, v in new_dict.items():
        print("{}: {}".format(k, v))
