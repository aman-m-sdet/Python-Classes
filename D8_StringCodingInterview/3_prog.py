#WAP to reverse the content of string using while loop?

s= input("enter the string:")
output =""
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)