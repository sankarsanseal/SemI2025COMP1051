

str1=input("enter a word:")
n=str1.upper()
m=n[::-1]
if n==m:
    print("palindrome",m)

else:
    print("not palindrome",m)
