#TUPLE  -"( )"   -(same as list) - order is imp, duplicate allowed -Immutable
#read inly version of list is TUPLE

#1. scenerio
K =(10,20,30,40)
print(type(K))
print(K[0])
print(K[-1])
print(K[1:4])

#2. scenerio
#Tuple K =( ,)  empty tuple "," is imp
# single value is tuple should end with ","
Z=(10)
print(type(Z))  # <class 'int'>
Z=(10,)
print(type(Z))  # <class 'tuple'>