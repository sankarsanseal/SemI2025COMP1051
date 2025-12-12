'''
Description: A Program To Find The Sum Of The Series: S= X + (X**2)/2! + (X**3)/3!+....+(X**n)/n!
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

var= float(input("Enter Value Of \"X\":"))


power= int(input("Enter Value Of Power And Factorial (\"n\"):"))


fact= 1


l=[]



for p in range(1,power+1):

    fact=fact*p

    val= (var**p)/fact
    
    l.append(val)


print(f"The Sum Of The List Is:{sum(l)}")