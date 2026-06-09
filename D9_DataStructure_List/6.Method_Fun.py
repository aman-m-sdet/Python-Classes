#imp methods and function  for list

# len(), count()  & index()
# Python inbuild functions
#len() :  returns the no/- of elements present in the list
#count(): returns the no/- of occuranceof specified emlement present in list
#index(): returns elelment present first occurance of the specified item

print("len() ......")
l=[10,20,30]
l1 = len(l)
print(l1 )     #3


print("Count() ......")
k=[10,20,30,10,20,30,10,20]
print(k.count(10))   #3
print(k.count(20))   #3
print(k.count(30))   #2


print("Index() ......")
s =[1,1,2,3,5,4]
x=int(input("Enter element to find : "))
if x in s:
    print('{} present at index:{}'.format(x,s.index(x)))
else:
    print(x,("not available in list"))
    