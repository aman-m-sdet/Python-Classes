#WAP to reverse the internal content of each word?
# input ="aman software solution"
# output ="nama erawtfos noitulos"

s= input("enter the string:")
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
    output=" ".join(l1)
    print(output)