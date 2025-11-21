'''

Description: Find the factorial of N.[N!=1*2*3*...*(N_1)*N]
Create Date: 17 November 2025
Author: Saptaparna De Sarkar
Semester: I
Course code: COMP 1051
Subject : Computer Science

'''
n=int(input("enter a no."))
f=1
for i in range(1,n+1):
    f*=i
print(f)
