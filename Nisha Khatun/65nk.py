'''

Description: Create a list with 10 integers. Show the original list and the list in reverse orde
Create Date: 20 November 2025
Author: Nisha
Semester: 1
Course Code: COMP 1051
Subject: Computer Science

'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1,9):
    list.append(i * 10)
print("original list:", list)
list.insert(1,5)
list.insert(3,8)
print("list after insertions:", list)
lrngth = len(list)
print("length of the list:", length)
mid = length // 2
print("first half of the list:",
list[:mid])
print("second half of the list:",
list[:mid])
