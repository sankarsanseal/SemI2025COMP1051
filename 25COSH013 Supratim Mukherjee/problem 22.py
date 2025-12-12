'''
Description: A Program To Find The Sum Of The Series: S= X + X**2 + X**3 +....+X**N
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

var= float(input("Enter The Value Of \"X\":"))

power= int(input("Enter The Value Of Power(\"n\"):"))


l=[]



print("The Series Is:",end=" ")



for p in range(1 ,power+1):


     l.append(var**p)
    



print("The Sum Of The Series Is:",sum(l))        

