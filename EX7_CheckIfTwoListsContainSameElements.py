# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:03:06 2023

@author: bop
"""
def same_list(a, b):
    if set(a) == set(b):
        return 1
    else:
        return 0


first = [1, 4, 9, 16, 9, 7, 4, 9, 11]
second = [11, 11, 7, 9, 16, 4, 17]

if same_list(first, second) == 1:
    print("Lists contain the same values.")
else:
    print("Lists does not contain same values.")