# tRAVERSING --> VISITING
l =[0,1,2,3,4,5,6,7,8,9,10]

#1. By using While Loop
print("While loop.......")

i=0
while i<len(l):
    print(l[i])
    i=i+1

#2. Byusing  for loop
print("for loop.......")

for x in l:
    print(x)

#3.Tpo print only even num
print("only even numbers using for loop.......")


for x in l:
    if x%2 ==0:
        print(x)


#4. to print element by list index wise
l = [10, 20, 30, 40, 50, 60]
i = 0
while i < len(l):
    print("The element present at +ve index:{} and at -ve index:{} is {}".format(i, i-len(l), l[i]))
    i += 1