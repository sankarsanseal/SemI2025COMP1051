'''
Description: A Program To Show The Even Integer Numbers On A List
Create Date:  November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


l=[]

for i in range(6):

    val=int(input("Enter Number:"))

    l.append(val)


even=[]

for e in l:

    if e % 2==0:

        even.append(e)

print("Even Integer List:",even)