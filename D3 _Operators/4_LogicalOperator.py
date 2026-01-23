#Logical Operators [ and , or, not]


#1. For Boolean type
# and  --> returns True if bot arguments are true
print(True and True)   # True
print(True and False)  # false
print(False and True)  # flase
print(False and False) # False

#or  --> returns true if one argument is true
print(True or True)   # True
print(True or False)  # true
print(False or True)  # true
print(False or False) # False

#Not  --> complement reverse
print(not True)    #false
print(not False)   #true

#example:
username=input("enter username:")
password= input("enter password:")
if username =="aman" and password =='Admin@123':
    print("valid user")
else:
    print("invalid user")


#2. For  non Boolean type 
# x and y   --> results is x & y but not boolen type
# 0 means false, non zero means true
# empty strig [ list,set,tuple,dict --false]

#example  x=10 (true) and y =20 (false)
print(10 and 20)  #20 false
print("durga" and "soft")  # soft (true) 

#x or y  -->results x | y
#example  x- true result x,   y- false resule y
print(10 or 20)    #10 (true)
print([] or "durga")  # durga 

#not - for non boolena type
#resiults is always boolean
print(not "aman")  #false
print(not "")   #true
print(not 0)  #true
print(not 10)  # false

