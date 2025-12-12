'''
Description: A Program To Print Sum Of Fibonacci Series
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


l=[]

for i in range(n):

    l.append(a)
   
    c=a+b
    a=b
    b=c
    
print(f"The Sum Of The Fibonacci Series Is:{sum(l)}")
    
