'''
Description: A Program To Print Fibonacci Series 
Create Date: 24 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


n= int(input("Enter How Many Terms You Want In Fibonacci Series:"))

a=0
b=1


print("The Series Will Look Like This:")



for i in range(n):
    
    print(a,end=" ")

    c=a+b
    a=b
    b=c
    

    