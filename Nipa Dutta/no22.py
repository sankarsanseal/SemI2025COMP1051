n=int(input("enter any term"))
x=int(input("enter a no."))
s=0
for i in range(1,n+1):
    s+=(x**i)/i
print(s)
