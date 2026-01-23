#Bitwise Operator [ bitwise AND (&) , Bitwise OR (|) ,Bitwise X-OR(^) , Bitwise complient (~), Bitwise leftshift(<<),Bitwise rightshift (>>)]
#applicale only for int and bool types

#bitwise AND (&) --> if both are 1 the result is 1 otherwise 0
#Bitwise X-OR(^) , --> atlease bit is 1 then reult is 1 other wise 0
#Bitwise complient (~),  -->if both bits are diff then rest is 1 or else 0

print( True & True)  #true
print(True & False)  # false
print(False & False) #false


print(True | False) #true
print(True | True)  #true

print(True ^ True) #false
print(True ^ False) #True

#print(~True => ~1)

print(True << 2) #4
print(True >>2)    #0