#DICT -"{ key :value}" pair  -order is not required -duplicate not allowed -hetrogenous objects
# Only Differ is FrozenSet is "IMMUTABLE" (cannot modify)
#################################################################################
#Syntax : d={K1:V1, K2:V2, K3:V3...... }    Example:
# 1st type:
D={100:'Aman',200: 'Anjum'}
print(type(D), D)   #<class 'dict'> {100: 'Aman', 200: 'Anjum'}

#2nd Type:
D[400] ="Midhat"
D[500] ="Haider"
print(D)            #{100: 'Aman', 200: 'Anjum', 400: 'Midhat', 500: 'Haider'}

# Duplicates key not allowed, value alowed --> no error dup not allowed, id will replace with value.
D[100] ="Muzzu"
print(D)            #{100: 'Muzzu', 200: 'Anjum', 400: 'Midhat', 500: 'Haider'}     


#Conclusion
#Gropu of key pair
#Order not allowed
#duplicate keys not allowed
#duplicate values allowed
#hetogenous obj acceptable
#mutable (changes allowed)
#Index/slice is not acceptable