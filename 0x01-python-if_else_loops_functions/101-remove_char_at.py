#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str):
        return str
    elif n < 0:
        return str
    else:
        str2 = ""
        for k in range(0, n):
            str2 = str2 + str[k]
        for k in range(n + 1, len(str)):
            str2 = str2 + str[k]
        return str2
