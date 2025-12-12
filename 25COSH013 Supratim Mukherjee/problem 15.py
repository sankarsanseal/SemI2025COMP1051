'''
Description: A Program To Find The Largest Among The 3 Numbers
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]

for i in range(3):

    val=float(input("Enter A Number:"))

    l.append(val)

l.sort()


print("The Largest Number Is:", l[2])