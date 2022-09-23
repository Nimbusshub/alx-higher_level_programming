#!/usr/bin/python3

"""Python script that finds
peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find the peak of integer"""

    if list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    li = list_of_integers
    if len(li) == 2:
        return max(li)

    length = len(li)
    mid = length // 2
    midPoint = li[mid]

    if li[mid + 1] < midPoint and midPoint > li[mid - 1]:
        return midPoint
    elif li[mid - 1] > midPoint:
        return find_peak(li[:mid])
    else:
        return find_peak(li[mid + 1:])
