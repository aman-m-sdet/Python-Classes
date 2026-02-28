#checking type of character present in the string:
#1) s.isalnum()
#2) s.isalpha()
#3) s.islower()
#4) s.isupper()
#5) s.isdigit()
#6) s.istitle()
#7) s.isspace()

print("Aman123" .isalnum())
print("Aman123".isalpha())
#ex1:
#WAP to check 2 characters ntered from keyboard?
print("###Program###")
s=input("enter any character:")
if s.isalnum():
    print("It is is alpha numeric character.")
    if s.isalpha():
        print("it is alphabetic.")
        if s.islower():
            print("it is lower case")
        else:
            print("it is upper case")
    else:
        print("it is digit")
elif s.isspace():
    print("it is space character")
else:
    print("it is non spce character")