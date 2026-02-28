#WAP to print character present at even index & odd index seperate for the given string
S ="amansoft"

#char present at even index
i=0
print("character present at even index:")
while i<len(S):
    print(S[i])
    i= i+2

#char present at odd index
i=1
print("Character present at odd index:")
while i<len(S):
    print(S[i])
    i=i+2

#method 2: Using slice :
S= "amansoft"
#S[0::2]
print("Character present at enven index:", S[::2])
print("character present at odd index is:", S[1::2])