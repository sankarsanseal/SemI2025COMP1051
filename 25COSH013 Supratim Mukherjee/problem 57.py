'''
Description: A Program To Count The Number Of Occurrences Of A String From A Supplied Paragraph
Create Date: 15 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

string= input("Enter Paragraph:")

search= input("Enter The Word You Want To Count:")

string_a=(string.lower())


search_lower= search.lower()




string_b=(string_a.count(search_lower)) 


print(string_b)