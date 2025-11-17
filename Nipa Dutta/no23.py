n=int(input("enter any term"))
x=int(input("enter a no."))
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=x**i
    else:
        s-=x**i
print(s)
