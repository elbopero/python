# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:48:42 2023

@author: bop
"""



import random

numbers = []
create_number = 0

while len(numbers) < 20:
    create_number = random.randint(0, 99)
    numbers.insert(len(numbers), create_number)
    
for number in numbers:
    print(f"{number}", end=" ")
    
numbers.sort()


print("\n-----------------------------------------------------------------")

for number in numbers:
    print(f"{number}", end=" ")