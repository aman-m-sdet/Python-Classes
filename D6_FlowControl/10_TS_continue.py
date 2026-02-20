# Transfer Statement: continue Statement:
# To ship he iteration and continue with next iteration we use continue statement.

#ex.1
for i in range(10):
    if i%2 ==0:
        break
    print(i)     # 

#ex2:
for i in range(10):
    if i%2 ==0:
        continue
    print(i)     # 13579


# ex2:
cart = [10,20,30,400,500,900,600]
for item in cart:
    if item >500:
        print("insurance is required, skip!")
        continue
    print("processing item", item)
#Ex3:
l =[10,20,30,0,4,0,30]
for x in l:
    if x==0:
        print("how we can divid with zero")
        continue
    print('100/{}={}'.format(x,100/x))





#with out loop we canot use continue syntax.
# it is imp, if we need to use continue & break stmt it should be in loop.