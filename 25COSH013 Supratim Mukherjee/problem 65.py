'''
Description: A Program To Create A List Of Integers And Delete The Even Elements
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]

how_many= int(input("Enter How Much Things Should Be Added In The List:"))

for i in range(how_many):

    val= int(input("Enter A Number:"))

    l.append(val)

print("The List Of Integers Is:",l)

#Deleting Even Elements


odd_list=[]

for odd in l:

    if odd % 2 !=0:

     odd_list.append(odd)

print("The Odd List Is:",odd_list)