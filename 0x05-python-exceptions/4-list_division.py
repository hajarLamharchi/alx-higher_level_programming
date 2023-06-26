#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                new_list.append(0)
    except IndexError:
        new_list.append(0)
        print("out of range")
    finally:
        return new_list
