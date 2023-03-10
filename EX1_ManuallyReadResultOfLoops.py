# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 22:38:54 2023

@author: bop
"""

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range (10):
    total = total + a[i]
    
print(total)

total = 0
for i in range(0, 10, 2):
    total = total + a[i]
    
print(total)

total = 0
for i in range(1, 10, 2):
    total = total + a[i]
    
print(total)

#total = 0
#for i in range(2, 11):
#    total = total + a[i]
    
print(total)
    
total = 0
i = 1
while i < 10:
    total = total + a[i]
    i = 2 * i
    
total = 0
for i in range (9, -1, -1):
    total = total + a[i]
    
print(total)

total = 0
for i in range (9, -1, -2):
    total = total + a[i]
    
    
print(total)