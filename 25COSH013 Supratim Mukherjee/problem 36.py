'''
Description: A Program To Check Whether A Number Is Armstrong Number Of Order Three Or Not
Create Date: 28 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]


num= input("Enter Any Three Digit Number:")


for i in num:


    val= (int(i)**3)
    l.append(val)
    


if sum(l)== int(num):

    print("The Number Is An Armstrong Number Of Order Three!")

elif int(num) != 3:

    print("Three Digit Numbers Only!!!")


else:
    print("The Number Is Not An Armstrong Number!!!:")
