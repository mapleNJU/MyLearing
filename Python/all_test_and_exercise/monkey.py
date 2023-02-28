from random import shuffle
from itertools import izip, tee


def in_order(my_list):
    """Check if my_list is ordered"""
    it1, it2 = tee(my_list)
    it2.next()
    return all(a <= b for a, b in izip(it1, it2))


def bogo_sort(my_list):
    """Bogo-sorts my_list in place."""
    while not in_order(my_list):
        shuffle(my_list)