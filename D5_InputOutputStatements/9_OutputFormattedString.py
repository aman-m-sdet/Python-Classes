#formatted string
# %i --> signed decemil Value
# %d --> signed decimal Value
# %f --> float Value
# %s --> String 
# any other objects like list,set ,...etc

# Syntax : (formatted string %(variable list))

#Ex1:
a=10
print('a value:%i' %a)     #a value:10

#Ex2:
x=10
y=20
z=30
print('x=%d y:%d z:%d' %(x,y,z))  #x=10 y:20 z:30

#Ex3:
name='durga'
marks=[10,20,30,40]
print("hello %s your marks list is %s" %(name,marks))  #hello durga your marks list is [10, 20, 30, 40]

#Note : Formatted string is powerful than replacement operator

price =70.678
print("price value ={}".format(price))   #price value =70.678
print("price vlaue = %f" %price)         #price vlaue = 70.678000

#if i need only 3 decimal point
print("price value =%.3f" %price)        #price value =70.678