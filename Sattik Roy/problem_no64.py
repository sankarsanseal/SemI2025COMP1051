'''
description: create a dynamic size list using apend().use insert () to insert at the 1st and the 4th location.
show the length of the list. use slicing to show the first and the second half of the list separately.
create date:2 nov 2025
semester:1
course code: 1051
subject: computer science
'''

n=int(input("enter the length of the list"))
print(f" enter {n} values")

my_list=[]
for i in range (0,n):
    value=int(input())
    my_list.append(value)

print(my_list)
