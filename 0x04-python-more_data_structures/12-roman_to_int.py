#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    n = len(roman_string)
    result = 0
    r = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}
    for i in reversed(range(n)):
        if i < n - 1 and r[roman_string[i]] < r[roman_string[i + 1]]:
            result -= r[roman_string[i]]
        else:
            result += r[roman_string[i]]
    return result
