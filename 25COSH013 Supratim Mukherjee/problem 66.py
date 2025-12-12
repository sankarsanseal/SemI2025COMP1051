'''
Description: A Program To Find The Sum And Avarage Of A List Of Integers
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

# Create List

l=[]

for i in range(6):

    val=int(input("Enter Number:"))

    l.append(val)

print("The List Is:", l)


# Sum Of List

sum_of_list= sum(l)

print("The Sum Of The List Is:", sum_of_list)


#Avarage Of List


print("The Avrage Of List Is:", sum_of_list/len(l))


