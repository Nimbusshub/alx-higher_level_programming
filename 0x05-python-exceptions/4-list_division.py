#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = list()
        i = 0
        cont = 0
        while i < list_length:
            try:
                cont = my_list_1[i] / my_list_2[i]
            except TypeError:
                cont = 0
                print("wrong type")
            except ZeroDivisionError:
                cont = 0
                print("division by 0")
            except IndexError:
                cont = 0
                print("out of range")
            new_list.append(cont)
            i += 1
    finally:
        return new_list
