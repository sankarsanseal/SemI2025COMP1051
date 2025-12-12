
'''
problem no :29
description :Find the HCF and LCM of two numbers.
create date : 24/11/2025
author :Debjit Das
semester : 1
subject : computer science
'''
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // hcf(a, b)

 

num1, num2 = 12, 18
print("HCF:", hcf(num1, num2))
print("LCM:", lcm(num1, num2))


