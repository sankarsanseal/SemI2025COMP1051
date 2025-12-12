'''
Description: A Program To Check If Two Strings Are Anagram Or Not
Create Date: 16 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

string_a= input("Enter Something:")


string_b=input("Enter Something:")


string_lower_1=(string_a.lower())


string_lower_2=(string_b.lower())


lists_1= list(string_lower_1)


lists_sorted_1= (lists_1.sort())


lists_2= list(string_lower_2)


lists_sorted_2= (lists_2.sort())


lists_conclusion= lists_1==lists_2


print("\"The Two Words Are Anagram\" The Statement Is:", lists_conclusion)


