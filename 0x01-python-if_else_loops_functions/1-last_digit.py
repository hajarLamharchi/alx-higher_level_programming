#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    print("Last digit",
          " of {} is {} and is".format(number, last_digit),
          " greater than 5")
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif last_digit < 6:
    print("Last digit of {} is {}".format(number, last_digit),
          " and is less than 6 and not 0")
