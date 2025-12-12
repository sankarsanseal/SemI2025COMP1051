'''
Description: A Program To Create A List With 10 Integers And Show The Original List And In Reverse Order
Create Date: 16 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l= []

for i in range(0,10):

    val=int(input("Enter Number:"))
    l.append(val)

print(l)

l.reverse()

print(l)
