'''
Description: A Program To Reverse A Number
Create Date: 26 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]


num=input("Enter A Number:")

print("The Reversed Version Of The Number Is:",end="")

for i in num:

    l.append(int(i))

l.reverse()


for j in l:

    print(j , end="")