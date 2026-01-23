# Operators:
# a person who operates is called operator

# ARTAHAMATIC OPERTORS: [+ , - , * , / , %]
# / --> normal Division operator
#// --> Floor Division Operator
# * --> multiplication Operator
# ** -->Exponential or power operator -->new in python
# Example:

a=10
b=20
print(a+b)  #30
print(a-b)  #-10
print(a*b)  #200
print(a/b)  #0.5
print(a%b)  #10

print(10/2) #  5.0 --> floating point value
print(10//2) # 5 --> intger
print(10/3) # 3.33333--
print(10//3) # 3

# normal Division
print(10/3)  # 3.3333
print(10.0/3) # 3.333

# floor Division
print(10//3) # 3 
print(10.0//3) # 3.0

#multiplication
print(11*3) # normal 33
print(10**2) # --> 10squar =100
print(3**3)   #--> 3cube= 27 

#fro string + op for both int and str
print(10+2)
print("aman"+"soft")   # amansoft
#print('aman'+10) # --> Type error
print('aman'+'10') #aman10
print("aman"+str(10)) #aman10

# for String    [ str+str , str*str, int*str]
print("Aman"*3)   #AmanAmanAman
print(2*'aman')   #amanaman
#print("aman"*"Soft") #---> error
#print("aman"*'3')  # --error
print("aman"*int(2)) #amanaman

#zero division error
#print(10/0) # ZeroDivisionError: division by zero
#print(10.0/0)
#print(10//10)
#print(10.0//0)
#print(10%0)

# bool for string
print("durga"* True)  # durga
print('durga'*False)   # '   '  empty 