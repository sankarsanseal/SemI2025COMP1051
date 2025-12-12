'''
Description: A Program To Search A Given Key Value From A List Of 10 Integers
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]

for i in range(10):
 
    val=int(input("Enter A Number:"))

    l.append(val)


search= int(input("Enter The Number You Want To Find On The List:"))


for i in l:
    
    if search==i:
        print("Found")
        
        break

    else:
        print("Not Found")

        break
   

