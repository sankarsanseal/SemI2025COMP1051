'''
Description: A Program To Create A Dynamic Size List And More
Create Date: 20 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

# Dynamic Size List Code

l=[]

how_many= int(input("Enter Much Things Should Be Added In The List:"))

for i in range(how_many):

    val=int(input("Enter Number:"))

    l.append(val)

print("Your List:",l)


# Insert Number To 1st And 4th Location

num_1= int(input("Enter The 1st Number You Want To Insert:"))

l.insert(0, num_1 )

num_2= int(input("Enter The 2nd Number You Want To Insert:"))

l.insert(3,num_2)

print("New List Is:",l)

# Show The Length Of List

print("The Length Of The List IS:",len(l))

#Split The List On Two Halfs

half= len(l) // 2

print("1st Half Of List Is:", l[ :half])

print("The 2nd Half Of The String Is:", l[half: ])