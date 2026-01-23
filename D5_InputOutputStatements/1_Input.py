#1. Raw_Input():
# can be used to read end user data
# it always provide in the form of string  , compulsory type casting

#x= raw_input("enter some value:")   # ra_input i n python2
#y =int(x)
#print(type(x))
##############################################################
#2. input( ):  this function is not required the type casting

x = input("enter some value:")
print(type(x))

#Demo Prog: Reade ip date from keyboard
 #1st method:
x=input("enter first number:")
y=input ("enter second number:")
i=int(x)
j=int(y)
print("sum is:", i+j)

#2nd method
 #1st method:
x=int(input("enter first number:"))
y=int(input ("enter second number:"))
print("sum is:", x+y)

#Deom2 Prog: WAP to read empdata from keyboard and print output
eno =int(input("enter Emp no:"))
ename=(input("enter Ename:"))
esal=float(input("enter salary:"))
eadd=input("enter address: ")
married= eval(input("emp married? [True | False]:"))
print(eno)
print(ename)
print(esal)
print(eadd)
print(married)

