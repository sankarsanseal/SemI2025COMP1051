'''
Description: A Program To Check Whether A Number Is A Perfect Number Or not
Create Date: 28 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


l=[]

num= int(input("Enter Any Number:"))


for i in range(1,num+1):

    val= num % i

    if val == 0:

        l.append(i)


l.pop(-1)

if sum(l) == num:

    print("The Number Is A Perfect Number!!")

else:
    print("The Number IS Not A Perfect Number!!")