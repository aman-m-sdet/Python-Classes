#Equity operation for list object
#1. (==)
#2. (!=)

l1=["dog","cat","rat"]
l2=["dog","cat","rat"]
l3=["DOG","CAT","RAT"]
l4=['cat','Rat','dog']
print(l1==l2)   #True
print(l1==l3)   #false
print(l1==l4)   #false
print(l2==l4)

print(l1!=l4)   # True

# Relations Operator
# (<), (>), (<=), (>=)
l1=[10,20,30,40]
l2=[50,60]
print(l1<l2)    #true
print(l1<=l2)   #true
print(l1>l2)    #false
print(l1>=l2)   #false

#string:
l1=["Ramba","Ramya"]
l2=["Simran","samanta"]
print(l2>l1)    #true


#membership Operator
#(in) , (not in)
print("membership operator")
l1=[10,20,30,40]
print(10 in l1)        #true
print(50 not in l1)    #true 
print(70 in l1)        #false

