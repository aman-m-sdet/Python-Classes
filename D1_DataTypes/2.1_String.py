#string str
s="aman"
print(type(s))
k='t'
print(type(k))
T='''TKS'''
print(type(T))

A="aman is 's/w' Engineer"
print(A)
A='aman is "s/w" Engineer'
print(A)
A='''aman is 's/w' Engineer & "Tech" Engineer'''
print(A)

#str datatype:   positive and negative INDEX
K="AMAN"
print(type(K))
print(K[0])
print(K[3])
#print(K[10])     IndexError: string index out of range
print(K[-2])
print(K[-1])

#str datatype:  SLICE Operator
S='abcdefghijklmnopqrstuvwxyz'
print(S[3:9])
print(S[:5])
print(S[3:])
print(S[:])

S = "Aman"
output = S[0].upper()+S[1:]
print(output)

#reverse the string
print(S[0].upper()+S[1:3]+S[3:4].upper())
print(S[::-1])
rev=(S[::-1])
result=rev[0].upper()+rev[1:3] +rev[3].upper()
print(result)

print(S[0+len(S)-1]+S[-1].upper())
print(S[0+len(S)-1])

#da#str datatype: + and * operators
s= 'durga' +'soft'
print(s)

#s= "durga"+10
#print(s)     #TypeError: can only concatenate str (not "int") to str

s="durga"+'10'
print(s)

# * Operators with string
s='durga'*3
print(s)

s=2*'aman'
print(s)

# s= "aman" * "Durga"
# print(s)              #TypeError: can't multiply sequence by non-int of type 'str'

print('#'*10)
print("AMAN MUZAMMIL")
print('#'*10)
