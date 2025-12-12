
l=[]
n= int(input("Enter The Length Of Fibonacci Series:"))


a=0
b=1
print(0)
for i in range(1,n+1):
    

    a,b=b,a+b


    print(a)
    l.append(a)

s=sum(l)
print("the sum is",s)


