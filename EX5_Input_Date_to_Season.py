# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:04:24 2023

@author: bop
"""
import re

spring = ["april", "may"]
summer = ["july", "august"]
fall = ["october", "november"]
winter = ["january", "february"]

user_input = input("Enter date, example -> January 20: ").lower()

c = 0

month = ""
days = 0

daysreg = re.findall("\d", user_input)
days = int("".join(daysreg))

c = 0

while(user_input[c].isalpha()):
    month += user_input[c]
    c += 1


if month in spring:
    print("Date you entered is in spring.")
elif month in summer:
    print("Date you entered is in summer.")
elif month in fall:
    print("Date you entered is in fall")
elif month in winter:
    print("Date you entered is in winter")
elif month == "march":
    if days >= 20:
        print("Date entered is in spring.")
    else:
        print("Date entered is in winter.")
    
print(month)
print(days)