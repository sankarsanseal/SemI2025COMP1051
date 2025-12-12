'''
Description: A Program To Make A Tuple With 6 Elements And More
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

tup_as_list= []

for i in range(5):

    val_1=float(input("Enter Number:"))
    

    tup_as_list.append(val_1)

print("The Tuple Is:",tuple(tup_as_list))


for e in range(2):


 val_2= float(input("Enter Number:"))

 tup_as_list.append(val_2)


print("The New Tuple Is:",tuple(tup_as_list))


tup_as_list.pop(2)


print("The 3rd Element Is Removed:",tuple(tup_as_list))