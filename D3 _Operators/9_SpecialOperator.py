#Special Operator

#1. identity operator   [#"is" , "is not"]
#r1 is r2   --> True if both refer to same obj
#r1 is not r2 -->true if both ref are nt pointing to same obj

a=10
b=10
print(a is b)    #true
print(a is not b) #false 

l1=[10,20,30,40]
l2=[10,20,30,40]
print(id(l1))  #2733172054208
print(id(l2))  #2733172208576

print(l1 is l2)   # false
print(l1 is not l2) # true
print(l1 == l2)  #true

#2. Membership operator   [#"in" , "not in"]
# to check membership operator a in sequence -->true  ,  a not in sequence -->true

s="hello learning python is easy"
print("h" in s)  #True
print("python "in s)  #true
print("aman" in s)  # false
print("is" not in s) # false

l =["suny", 'bunny',"honey","chinni"]
print("sunny" in l) #false
print("chinni" in l) # true
print("ruby" not in l)  #true
print("bunny" not in l)  # false