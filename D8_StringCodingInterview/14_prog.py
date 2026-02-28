#WAP to remove duplicates from the given string?


#method:1
s=input("Enter the string including duplicates char: ")
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)


#method:2
s= input(" enter duplicate cahracters:" )
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
output=''.join(l)
print(output)

#method: 3 : but not in order
s=input("enter duplicate string:")
s1=set(s)
output=''.join(s1)
print(output)