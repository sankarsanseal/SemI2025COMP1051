
'''
description: Print the Fibonacci Series: - 0 1 1 2 3 5 8 13 21 …. n
create date: 25 november 2025
author: Dabjit Das
semister: 1
course code: comp 1051
subject: computer science
'''

a,b = 0,1
n=int(input("enter a number"))

for i in range(0,n+1):
    print(a)
    s=a+b
    
    a=b
    b=s
    

