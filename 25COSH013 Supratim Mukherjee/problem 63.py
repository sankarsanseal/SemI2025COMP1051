'''
Description: A Program To Check If A List Is Empty Or Not
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

l=[]

how_many= int(input("How Much Things Need To Be Added In The List?:"))

for i in range(how_many):

 val= int(input("Enter Something(Nmbers Only):"))

 l.append(val)
 
print(l)

empty_list= []

empty=empty_list==l


print("\"The List Is Empty\" The Statement Is:", empty)