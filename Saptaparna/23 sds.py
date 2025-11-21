'''

Description: Find the Sum of the series: S=-x+x^2-x^3+....x^n, where value of x and n are unknown
Create Date: 17 November 2025
Author: Saptaparna De Sarkar
Semester: I
Course code: COMP 1051
Subject : Computer Science

'''
n=int(input("enter a term"))
x=int(input("enter a number"))
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=x**i
    else:
        s-=x**i
print(s)
