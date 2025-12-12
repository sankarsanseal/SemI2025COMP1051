'''
Description: A Program To Find The Sum Of The Series: - X + X**2 -X**3....X**n
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


var= float(input("Enter Value Of \"X\":"))


power= int(input("Enter Value Of Power (\"n\"):"))

l_1=[]


l_2=[]




for p in range(1,power+1):

    if p % 2 == 0:
        l_1.append(var**p)

    else:
        l_2.append(var**p)


sum_1= sum(l_1)

sum_2=sum(l_2)


print(f"The Sum Of The Series Is:{sum_1-sum_2}")