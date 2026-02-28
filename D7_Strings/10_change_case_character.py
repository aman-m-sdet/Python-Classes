#Changing case of the character of string:

#1. upper() --> convert all characters to upper
#2. lower() --> convert all characters to lower
#3. swapcase() --> convert loweer to upper & upper to lower 
#4. title() --> convert evert 1st letter  to capital
#5. capitalize() --> only 1st characters to upper, all will be lower

#Ex1:
s="Learning Python"
print(s.upper())     #LEARNING PYTHON
print(s.lower())      #learning python
print(s.swapcase())   #lEARNING pYTHON
print(s.title())      #Learning Python
print(s.capitalize()) #Learning python

print('###WAP to check given 2 strings are equal or not?###')

s1=input("enter firat string : ")
s2=input("enter second string : ")
if s1==s2:
    print("both strings are equal")
else:
    print("both strings are not equal")

#2nd method
print("##2nd method##")
s1=input("enter firat string : ")
s2=input("enter second string : ")
if s1.lower()==s2.lower():
    print("both strings are equal")
else:
    print("both strings are not equal")

#WAP to check provided username and password are valid or not UN is case sensetive and psw is not cs.
print("###valid un & psd####")

un=input("enter user name: ")
pw=input("enter password: ")
if un.lower() == 'Aman' and pw =="Aman123":
    print("valid user")
else:
    print("invalid user")


#WAP to convert 1st and last char to upper case and all remaining in lower case of given string
print("### 1st and last is upper ####")
s=input("enter string:")
output = s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper()
print(output)   #BadshA