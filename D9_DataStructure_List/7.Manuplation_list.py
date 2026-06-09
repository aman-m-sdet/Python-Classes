#Manuplation elelments of list
# 1. append() - to add items at the end of the list
# 2. insert() - to insert item at specific index
# 3. extend() - to add all elements of given sequence to list
# 4. Remove() -  to remove specifed element from the list
# 5. pop() -    to remove retures last element from list
# 6. clear() -  to remove all elements from the list

#1. append()

print("append() methos- used at end of list")
l=[]
l.append(10)
l.append(20)
l.append(50)
l.append(40)
print(l)     #[10, 20, 50, 40]

# add which are divisible by 10 from 1-100
k=[]
for x in range(1,101):
    if x%10==0:
        k.append(x)
print(k)     #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#2. Insert()
print("Insert() -- specified position of index")
#p.insert(index,element)
p=[10,20,30,40]
p.insert(1,7777)
print(p)       #[10, 7777, 20, 30, 40]

p.insert(100,8888)
p.insert(-100,9999)
print(p)     #[9999, 10, 7777, 20, 30, 40, 8888]

#3. extend()
print("extend() -- to add all elements of given sequence of list")

#p1.extend(p2)
order1=["chicken","mutton","fish"]
order2=["KF","KO","RC"]
order1.extend(order2)
print(order1)       #['chicken', 'mutton', 'fish', 'KF', 'KO', 'RC']

#ex1
s1=[10,20,30]
s2=[40,50]

#s1.append(s2)
#print(s1)       #[10, 20, 30, [40, 50]]
#print(len(s1))  #4

s1.extend(s2)
print(s1)          #[10, 20, 30, 40, 50]
print(len(s1))     #5

#ex2:
d =[10,20,30]
#d.append("abc")
#print(d)           #[10, 20, 30, 'abc']

d.extend("abc")
print(d)            #[10, 20, 30, 'a', 'b', 'c']
print(len(d))       # 6


#4. Remove():
#print("Remove() -- to remove elements of given sequence of list")
m = [10,20,50,30,40,10,20,30,50]
m.remove(50)     # first occurance will be reoved
print(m)     #[10, 20, 30, 40, 10, 20, 30, 50]

#Ex1
m1=[1,2,3,4]
print("Before removal:", m1)
x= int(input("element to remove: "))
if x in m1:
    m1.remove(x)
    print("after removal:",m1)
else:
    print(x,"not available in list")

#Ex2:  remove all occurances

n1 = [1,1,1,2,2,2,3,4,5,3,5]
x =int(input("enter element to remove: "))
while True:
    if x in n1:
        n1.remove(x)
    else:
        break
print("After removal:" ,n1)

#4. Pop():
#print("Pop() -- to remove last element from given list")

x = [10,20,40,50,606,70,90]
print(x.pop())
print(x)

print(x.pop(1))
print(x)

#4. Clear():
#print("Clear() -- to remove all elements from the list")

y=[10,20,30,50,60,70,70,80,90,100]
y.clear()
print(y)   # []

