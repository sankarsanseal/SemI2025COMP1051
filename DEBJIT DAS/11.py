'''
Description: A Program To Calculate Amount Using Compound Interest
Create Date: 14 November 2025
Semester:1
Author: Debjit Das
Roll no: 25COSH002
Course Code:1051
Subject:Computer scince
'''

P=float(input("Enter The Principal In Rupee(s):"))

print("Rupee(s)")

R= float(input("Enter The Rate OF Interest Per Annum In (%):"))

print("%")


R= R/100


N= float(input("Number Of Times Interest Is Compounded In A Year:"))

print("Year")

T= float(input("Enter Time in Year(s)"))

A= P*(1+R/N)**(N*T)

print(A)