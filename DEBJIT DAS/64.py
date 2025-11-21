'''

'''
list1 = []

n = int(input("enter the number of elements in interger list:"))

for i in range(0,n):
    val=int(input("enter the element"))
    list1.append(val)
    
        
print(list1)
a =int(input("enter the index where you want to insert: "))
val=int(input("enter the element"))
list1.insert(a,val)
print(list1)
             
