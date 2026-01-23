#Range - epresent number form (0 to 10) or (100  to 1000)
# 
#################################################################################
#Syntax : range(10)
r=range(10)
print(type(r))   # <class 'range'>
print(r)         # range(0, 10)
for x in r:
    print(x)     #0 1 2 3 ..9

# form 1:  range(n)
r= range(20)
r1=range(100)
print(r,r1)    #range(0, 20) range(0, 100)

#form 2:  range(begin, end)  --> (begin to end-1)
r3 = range(1,10)
for x in r3:
    print(x)  #1 2 3 ...9

r4 = range(2,11)
for x in r4:
    print(x)  # 2 3 ...10  

#form 3: range(begin to end, increment/decrement value)
r5 = range(1, 30, 3)
print(r5)     #range(1, 30, 3)
for x in r5:
    print(x)  #1 4 7 10 13 16..28

r6= range(20, 10, -3)
for x in r6:
    print(x)  # 20 17 14 11

print(r5[0])   #1
print(r5[2])   #7

#conclusion
# sequence
#range(10)-form1 | range(2,20)-form2 |range(2,30,2)-form3
#order, inde,slice
#immutble