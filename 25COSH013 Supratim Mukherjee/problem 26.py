'''
Description: A Program To Find The Sum OF The Series: S= - X + (X**2)/2! - (X**3)/3!+....(X**n)/n!
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



l_even=[]

l_odd=[]

fact= 1

for p in range(1,power+1):

    fact= fact*p


    if p % 2 == 0:

        l_even.append((var**p)/fact)


    else:
        l_odd.append((var**p)/fact)



sum_even= sum(l_even)

sum_odd= sum(l_odd)


print(f"The Sum Of The Series Is{sum_even-sum_odd}")