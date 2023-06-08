#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    name = dir(hidden_4)
    name.sort()
    for i in name:
        if not i.startswith("__"):
            print(i)
