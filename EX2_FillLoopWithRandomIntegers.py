# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:04:17 2023

@author: bop
"""

import random

numbers = []

create_number = 0

while len(numbers) < 10:
    create_number = random.randint(1, 100)
    numbers.insert(len(numbers), create_number)
    
sum = 0
even_numbers = 0

for number in numbers:
    print(f"{number}", end=" ")
    sum += number
    
    if number % 2 == 0:
        even_numbers += 1

print("\n_____________________________________")    
print(f"The sum of all numbers = {sum}")
print("_____________________________________")
print(f"Number of even number in list = {even_numbers}")

even_list = []
odd_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.insert(len(even_list), number)
    else:
        odd_list.insert(len(odd_list), number)
        
print("_____________________________________")
print("Even list:")

        
for number in even_list:
    print(f"{number}", end=" ")
    
print("\n_____________________________________")
print("Odd list:")

for number in odd_list:
    print(f"{number}", end= " ")
    
i = 0

for number in numbers:
    if number % 2 == 1:
        numbers.remove(number)
        
print("\n_____________________________________")
print("Removing odd numbers from list")
for number in numbers:
    print(f"{number}", end=" ")