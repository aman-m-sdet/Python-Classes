#WAP to merge character of 2 str into single str by taking char alertnativily?
#input:  s1='Aman'   s2='Muzzu'

s1=input("enter 1st str:")
s2=input("enter 2nd str:")
i,j=0,0
output="" 
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)


#NOTE: for above, if length of s1 != s2, then we will get indexbound issue in that case how to handle
p1="AMAN"
p2="AM"
i,j=0,0
output=''
while i<len(p1) or j<len(p2):
    if i<len(p1):
        output=output+p1[i]
        i=i+1
    if j<len(p2):
        output=output+p2[j]
        j=j+1
print(output)

