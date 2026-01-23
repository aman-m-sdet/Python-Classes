# None - means NOTHING
# No Value assigned
#################################################################################
a = 10
a =None
print(type(a))   #<class 'NoneType'>

# functions:
def f1():
    return 10
x=f1()
print(x)   # 10

def f1():
    print("hello")
x=f1()
print(x)  # None

# None is also an object in python
a = None
print (id(a))  #140712594417656
print(type(a)) # <class 'NoneType'>

#throughout python only 1 None object is present
a = None
b = None
c = None
def f1():
    pass
d = f1()
print(id(a), id(b), id(c))  # 140712594417656 140712594417656 140712594417656
print(a, b,c)               # None None None