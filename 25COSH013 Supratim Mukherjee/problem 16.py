'''
Description: A Program To Check A Number Is Leap Year Or Not
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

year= int(input("Enter Year:"))

if year % 400 == 0:

    print("Leap Year")

elif year % 100 == 0:

    print("Not A Leap Year")

elif year % 4 == 0:

    print("Leap Year")

else:
    print("Not A Leap Year")