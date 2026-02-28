# string method to find  Substring:
    #1. index()    ------->
    #2. rindex()   <------
s ="ABCBA"
print(s.index('B'))  #1
print(s.rindex("B"))   #3
#print(s.index("z"))    #value error
#print(s.rindex("x"))   #value error

#ex:1   email_id '@' should be manatory
mail = input("enter your email_id:")
try:
    i=mail.index("@")
    print("email id contains '@' ")
except:
    print("Email id doesnot contain '@' ")
