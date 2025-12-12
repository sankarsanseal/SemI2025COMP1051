



str1=input("enter first string")
str2=input("enter second string")
copy_str1=str(str1)
copy_str2=str(str2)


#n=list(str1)
#m=list(str2)
for i in copy_str2:
     copy_str1=copy_str1.replace(i,"",1)

     
if len(copy_str1)==0:
    print(str1, "is anagram of",str2)
    


    

