# LIST   - order is imp, duplicate allowed
l=["aman",10,20,30,20,10,50,5,"durga"]
print(type(l))
print(l)
print(l[0])
print(l[3])
print(l[1:4])
print(l[-1])

z=[]
z.append(40)
z.append(20)
z.append(40)
#z.append(40,50,40,90)    #TypeError: list.append() takes exactly one argument (4 given)
z.append(30)
z.append(-50)
z.remove(40)
print(z)  

k=[10,20,30,40,50]
k[0]=222
print(k)

#TUPLE
