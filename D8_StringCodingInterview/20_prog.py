#WAP to ceck given string is polindrome or not
# a string is said ploindrome iff orginal string and it reversed string are equal

# Ex: eye, malayalam, level
s=input("enter some string:")
if s== s[::-1]:
    print("the given string is ploindrome")
else:
    print(" the string is not polindrome")
