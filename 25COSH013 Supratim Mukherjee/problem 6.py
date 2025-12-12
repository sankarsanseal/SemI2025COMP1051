'''
Description: A Program To Calculate Area Of A Tringe
Create Date: 14 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''




a=float(input("Enter The Length Of 1st Side Of Triangle:"))

print("Units")

b=float(input("Enter The Length Of 2nd Side Of Triangle:"))

print("Units")
c=float(input("Enter The Length Of 3rd Side Of Triangle:"))

print("Units")

s= (a+b+c)/2

A= (s*(s-a)*(s-b)*(s-c))**0.5

print("The Area Of The Triangle Is:",A ,"Units\u00b2")