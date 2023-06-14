#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    result = 0
    div = 0
    for i in range(len(my_list)):
        result += my_list[i][0] * my_list[i][1]
        div += my_list[i][1]
    return result / div
