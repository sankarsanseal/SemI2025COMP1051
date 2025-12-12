'''
description: create a list of  integers delet the even elements
create date: 21 november 2025
auther: Debjit Das
semister: 1
course code: comp 1051
subject: computer science
'''


list1 = []
even_list = []
n = int(input("enter the number of elements in interger list:"))

for i in range(0,n):
    val=int(input("enter the element"))
    list1.append(val)

print('before deletion the list',list1)

for i in list1:
    if i%2==0:
        
       even_list.append(i)
print('the even list before deletion',even_list)

for item in even_list:
    list1.remove(item)

print('the final list',list1)
