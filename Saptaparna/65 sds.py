'''

Description: Create a list of integers. Delete the even elements.
Create Date: 20 November 2025
Author: Saptaparna De Sarkar
Semester: I
Course code: COMP 1051
Subject : Computer Science

'''
numbers = [23, 45, 89, 76, 25]
numbers = [num for num in numbers if num %2!=0]
print ("list after deleting even elements:", numbers)
