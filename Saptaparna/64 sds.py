'''

Description: Create a dynamic size list using append (). Use insert () to insert at the 1st and 4th location. Show the length of the list. Use slicing to show the first and the second half of the list separately
Create Date: 20 November 2025
Author: Saptaparna De Sarkar
Semester: I
Course code: COMP 1051
Subject : Computer Science

'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1,9):
    list.append(i * 10)
print("original list:", list)
list.insert(1,5)
list.insert(3,8)
print("List after insertions:", list)
length = len(list)
print("length of the list:", length)
mid = length // 2
print("first half of the list:",
list[:mid])
print("second half of the list:",
list[mid:])
