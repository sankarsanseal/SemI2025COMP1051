'''
Description: A Program To Find If A Number Is Prime Or Unprime
Create Date: 22 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


num= int(input("Enter Number:"))


l=[]



if num==1:
 print("1 Is Not Prime Or Unprime!")



for i in range(1,num+1):

    if num > 1 and num % i==0:

        l.append(i)
    



if len(l) >= 3 or len(l)==1:
    
    print("The Number Is Unprime")

elif len(l)==2:
    
    print("The Number Is Prime")




