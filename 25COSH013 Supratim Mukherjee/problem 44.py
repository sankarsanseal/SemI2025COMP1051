'''
Description: A Program To Print A Half Pyramid Using Numbers
Create Date: 06 December 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]


num= int(input("Enter The Maximum Number You Want In The Pyramid:"))
 
for i in range(1,num+1):
    
    l.append(i)

    print(*l)
