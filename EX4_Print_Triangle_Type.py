# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:15:22 2023

@author: bop
"""

side1 = int(input("Enter length of first side: "))
side2 = int(input("Enter length of second side: "))
side3 = int(input("Enter length of third side: "))

all_equal = "equilateral"
two_equal = "isosceles"
non_equal = "scalene"

if side1 == side2 and side2 == side3:
    print(f"Triangle is of type: {all_equal}")
elif side1 == side2 and side2 != side3:
    print(f"Triangle is of type: {two_equal}")
elif side1 == side3 and side1 != side2:
    print(f"Triangle is of type: {two_equal}")
elif side2 == side3 and side2 != side1:
    print(f"Triangle is of type: {two_equal}")
else:
    print(f"Triangle is of type: {non_equal}")
    
