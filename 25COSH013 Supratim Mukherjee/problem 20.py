'''
Description: A Program To Print Sum Of The Series: 2 + 4 + 6 +....+N
Create Date: 21 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''


l= []


how_many= int(input("Enter The Last Value Of The Series:"))


for i in range(1,how_many+1):

    if i % 2== 0:

        l.append(i)

print("The Series Is:",end=" ")


for i in l:

    if i != how_many:

     print(i,end=" + ")

    else:
       print(i)
    
print("The Sum Of The Series Is:",sum(l))    