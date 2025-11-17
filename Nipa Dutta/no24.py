n=int(input("enter any term"))
x=int(input("enter a no."))
s=0
f=1
for i in range(1,n+1):
    f*=i
    s=(x**i)/f
print(s)
