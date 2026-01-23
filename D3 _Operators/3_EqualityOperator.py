
#Equality Operatior
#[ equal to( == ), (not equal to (!=)]
print(10==20)   #false
print(10 !=20)  #true

print(1==True)  #true
print(1==1)  #true
print(10==10.0)  #true
print("Aman"=="aman")  # False
print("Aman"=="Aman")  # true

print(10=="ama")  #false
print(10=='10')   #false  no type error will print

#chaining of equality operator
print(10==10==20==30==40)  # false
print(10==10==10==10)  # true

# difference between == and 'IS' operator
#== is ment for content
#is ment for reference

l1=[10,20,30]
l2=[10,20,30]
print(l1 is l2)   #False
print(l1==l2)    #true
l3=l1
print(l1 is l3)   # true