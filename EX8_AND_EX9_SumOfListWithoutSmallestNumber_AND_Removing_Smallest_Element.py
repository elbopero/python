# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:10:20 2023

@author: bop
"""

import random

def remove_min(numbers):
    smallest = numbers[0]
    
    for i in range(0, len(numbers), 1):
        if numbers[i] < smallest:
            smallest = numbers[i]
            
   # return smallest
    print(smallest)
    numbers.remove(smallest)

def sum_without_smallest(numbers):
    
    list_sum = 0
    smallest = numbers[0]
    
    print(numbers)
    
    for i in range(0, len(numbers), 1):
        list_sum = list_sum + numbers[i]
        
        if numbers[i] < smallest:
            smallest = numbers[i]
    
    small_sum = list_sum - smallest
    print(list_sum)
    return small_sum

numbers = []
create_number = 0

while len(numbers) < 10:
    create_number = random.randint(1, 100)
    numbers.insert(len(numbers), create_number)
    
small_sum = sum_without_smallest(numbers)
print(f"Sum of list without smallest number = {small_sum}")

remove_min(numbers)

print(numbers)