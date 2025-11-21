print("Hello world")
a=65
b=89
print(a+b)
print(a*b)

import math
c=6
gh=c*c
gh_root=math.sqrt(c)
print("Square of a number",gh)
print("Square root of a number=",gh_root)
print(2*(a+b))
print_diamond(4)
def print_diamond(n):
    for i in range(n):
    print(''*(n-i-1)+'*'*(2*i+1))
    for i in range(n-2,-1,-1):
        print(''*(n-i-1)+'*'*(2 * i *1))

