'''
Description: A Program To Check If The Product Of The Digits Of A Number Is Equals To The Number Or Not
Create Date: 26 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

import math



l=[]


num=input("Enter A Number:")


for i in num:

    l.append(int(i))
    
m=math.prod(l)


if int(num) == m:

    print("The Product Of The Digits Of A Number Is Equals To The Number")

else:
    print("The Product Of The Digits Of A Number Is Not Equals To The Number")