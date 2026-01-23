#ternary Operator
#urnaryoperator (~a) , BinaryOperator(a+b), 3 terneryoperator(condationaloperator)
#example:
a=10
b=20
c=30 if a>b else 40 #->ternary operator
#Syntx: c= 1st_value if cond else 2nd_value

#WAP to read int value & print min value Ternery op
a=input("Enter 1st value:")
b=input("Enter 2nd value:")
min = a if a<b else b
print("the min value", min)

#Nesting of ternery operator
a=input("Enter 1st no:")
b=input("Enter 2nd no:")
c=input('Enter 3rd no:')
min = a if a<b and a<c else b if b<c else c
print("min no: ", min)
max = a if a>b and a>c else b if b>c else c
print ("max no:", max)
