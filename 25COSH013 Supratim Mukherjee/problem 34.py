'''
Description: A Program To Find The Factors Of A Number
Create Date:28 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


num= int(input("Enter A Number:"))


print("The Factors Of The Number Is:",end=" ")

for i in range(1,num+1):

    num % i

    if num % i == 0 and i != num:

        print(i,end=",")

    elif i== num:

        print(i,end="")