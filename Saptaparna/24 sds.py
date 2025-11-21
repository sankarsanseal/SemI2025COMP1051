'''

Description: Find the Sum of the series: S=-x+(x^2/2!)+(x^3/3!)+....x^n!, where value of x and n are unknown
Create Date: 21 November 2025
Author: Saptaparna De Sarkar
Semester: I
Course code: COMP 1051
Subject : Computer Science

'''
n=int(input("enter a term"))
x=int(input("enter a number"))
s=0
f=1
for i in range(1,n+1):
    f*=i
    s+=(x**i)/f
print(s)
