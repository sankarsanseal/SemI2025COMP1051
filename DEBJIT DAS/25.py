
n = int(input("enter a tarm"))
x = int(input("enter any number"))
s = 0
f = 1
for i in range(1,n+1):
    f*=i
    if i%2==0:
        s+=(x**i)/f
    else:
        s-=(x**i)/f
    

print(s)
