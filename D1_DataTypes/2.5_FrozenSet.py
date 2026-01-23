#SET  -"{ }"  -order is not required -duplicate not allowed -hetrogenous objects
# Only Differ is FrozenSet is "IMMUTABLE" (cannot modify)
#################################################################################


#1. scenerio  --> Set is Mutable  Example
S={10,20,30,40,50}
print(type(S))    #<class 'set'>
print(S)          #{50, 20, 40, 10, 30}  -- unordered
S.add(60)
S.remove(10)
print(S)          #{50, 20, 40, 60, 30}


#2. scenerio  --> FrozenSet is IMMutable  Example
S={10,20,30,40}
fs=frozenset(S)   #<class 'frozenset'>
print(type(fs))

#fs.add(50)       # error  as FS is immutable
#fs.remove(10)    # error  as FS is immutable