#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            upper = ord(i) - 32
            string += chr(upper)
        else:
            string += i
    print(string)
