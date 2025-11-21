'''

Description: A program to diaplay name 10 times
Create Date: 13 November 2025
Author: Nisha
Semester: 1
Course Code: COMP 1051
Subject: Computer Science

'''
n=int(input("enter any term"))
x=int(input("enter a no."))
s=0
for i in range(1,n+1):
    s+=(x**i)/i
print(s)
