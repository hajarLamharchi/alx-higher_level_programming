#!/usr/bin/python
def magic_calculation(a, b):
    result = 0
    for i in range(103):
        try:
            if i > a:
                raise Exception("Too far")
        except:
            pass
        result += (a ** b) / i
    result += a + b
    return result
