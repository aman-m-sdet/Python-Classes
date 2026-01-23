# LIST -"[ ]"  - order is imp, duplicate allowed - mutable

#1. scenerio
l=["aman",10,20,30,20,10,50,5,"durga"]
print(type(l))
print(l)
print(l[0])
print(l[-1])
print(l[1:4])


#2. scenerio   .append() and .remove() 2 methods to add and remove to list
z=[]
z.append(40)
z.append(20)
z.append(40)
#z.append(40,50,40,90)    #TypeError: list.append() takes exactly one argument (4 given)
z.append(30)
z.append(-50)
z.remove(40)
print(z)    #[20, 40, 30, -50]


#3. scenerio   Replace the value for the position as list is immutable
k=[10,20,30,40,50]
k[0]=222
print(k)       #[222, 20, 30, 40, 50]


