'''
Description: A Program To Print The Series: 1 + 2 + 3 +....+N
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


n= int(input("Enter The Last Value(N) Of The Series:"))


for i in range(1,n+1):

    if i==n:
        print(i)

    else:
        print(i,end=" + ")