'''
Description: A Program To Check That The String Is Plaindrome Or Not
Create Date: 16 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

string_a=input("Enter Something:")

string_lower=(string_a.lower())

string_b= string_lower[::-1]


string_1= string_lower==string_b

print("\"The String Is Plaindrome\" The Statement Is:", string_1)