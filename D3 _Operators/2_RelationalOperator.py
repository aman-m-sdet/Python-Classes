# Relationship or comparision Operatos
# [ >, >=, < , <=]


# Int Type
a=10
b=20
print(a>b)   # False
print(a<b)   # True
print(a>=b)  #False
print(a<=b)  #true

#Str type
s1 ='a'
s2='b'
# how to find unicode of char  very important
print(ord('a'))   # 97  
print(ord('b'))   #98
print(ord('A'))   # 65  
print(ord('B'))   # 66
print(chr(97))    #a 


print(s1>s2)   #false
S1="aman"
S2 ="Anjum"
print(S1>S2)  # True

#Boolean type   [True -->1,  False -->0]
print(True>True)   #false
print(False>False)  #False
print(True>False)   #True

# print(10<'Durga')  int < string  #type erorr
# example:

a=10
b=20
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")

#chasing of relational operators
print(10<20)       #true
print(10<20<30)      #true
print(10<20<30)      #true
print(10<20<30<40)      #true
print(10<20<30<40>50)      #false

