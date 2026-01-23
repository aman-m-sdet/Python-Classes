#SET  -"{ }"  -order is not required -duplicate not allowed -growable & mutable
# - hetrogenous objects
################################################################################


#1. scenerio  -->order is not required
s1={1,2,3}
print(s1)    #{1, 2, 3}
s2={2,3,1}
print(s2)    #{1, 2, 3}
s3={3,2,1}    
print(s3)    #{1, 2, 3}   ---> all 3 s1,s2,s3 are equal Order it will take

S={12,20,30,40}
print(type(S))   # <class 'set'>
print(S)

#2. Scenerio --> duplicates removed
S={10,20,10,"AMAN",50,60}
print(S)      # {50, 20, 'AMAN', 10, 60}   duplicates removed

#print(S[0])    #type error
#print(S[1:4])  #type error


#3. adding and removing to set (allowed as set is mutable)
S.add(30)
print(S)     # {50, 20, 10, 'AMAN', 60, 30}

S.remove(50)
print(S)     # {20, 'AMAN', 10, 60, 30}


#4.  Scenerio  Type 
# K={} this is empty dict not empty set

K = {}
print(type(K))   #<class 'dict'>

S =set()       #here s=() --> this is tuple ,  here s=set() --> this is set
print(type(S))   # <class 'set'>