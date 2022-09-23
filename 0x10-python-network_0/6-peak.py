#!/usr/bin/python3
"""Python script that finds peak in a list of unsorted integers"""


from logging.config import listen


def find_peak(list_of_integers):
    """Find the peak of integer"""
    if list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        if len(list_of_integers) == 2:
            return max(list_of_integers)

        length = len(list_of_integers)
        mid = length // 2
        midPoint = list_of_integers[mid]

        if list_of_integers[mid + 1] < midPoint and midPoint > list_of_integers[mid - 1]:
            return midPoint
        elif list_of_integers[mid - 1] > midPoint:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid + 1:])
