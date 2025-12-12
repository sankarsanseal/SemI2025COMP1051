'''
Description: A Program To Find The Factorial Of N
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

n= int(input("Enter Number To Find Factorial:"))


print(n,"!")

fact= 1

for i in range(1,n+1):

    fact=fact*i

print("The Answer Is:",fact)