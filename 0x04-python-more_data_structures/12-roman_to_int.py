#!/usr/bin/python3
def roman_to_int(roman_string):
    n = len(roman_string)
    result = 0
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    for i in reversed(range(n)):
        if i < n - 1 and
        roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            result -= roman_dict[roman_string[i]]
        else:
            result += roman_dict[roman_string[i]]
    return result
