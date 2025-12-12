'''
Description: A Program To Calculate The HCF and LCM Of Two Numbers
Create Date: 24 November 2025
Name: Supratim Mukherjee
Roll no: 25COSH013
Semester:1
Course Code:COMP1051
Course Name: Python Programming
Subject:Computer science
'''

#HCF


 

n_1= int(input("Enter Number:")) 
n_2= int(input("Enter Number:")) 
 
s_1= set()

s_2= set()

for i in range(1,n_1+1):

    f_1= n_1 % i

    if f_1 == 0:

        s_1.add(i)



for j in range(1,n_2+1):

    f_2= n_2 % j

    if f_2 == 0:

        s_2.add(j)
        


s_3 = s_1.intersection(s_2)



print(f"The HCF Is:{max(s_3)}")




# LCM

print(f"The LCM Is:{(n_1)*(n_2) // max(s_3)}")
 


  







    


    