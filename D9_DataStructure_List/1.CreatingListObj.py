#1. Empty list Obj:
l=[]
print (type(l))   # <class 'list'>

#2. if we know data already:
l=[10,20,30]

# 3. Dynamic input:
#    l=(eval(input("Enter the list: ")))

#4. by using lsit function:

#ex1:
l=list('Aman')
print(l)     #['A', 'm', 'a', 'n']

#ex2:
l = list(range(0,10,2))
print(l)      #[0, 2, 4, 6, 8]

#5. split fuction:
s='learning python is easy'
l=s.split()
print(l)        #['learning', 'python', 'is', 'easy']
