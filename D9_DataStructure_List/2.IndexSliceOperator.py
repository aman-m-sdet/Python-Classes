#Accessing elements of list by using index and slice operators:-

#Accessing elements of lists:

#1 By using index operator?
l=[10,20,30,40,50]
print(l[0])   #10
print(l[1])  #20  
print(l[3])   #40
print(l[-1])   #50
# print(l[50])  # error out of range


#1 By using slice operator?
#syntax: l[begin:end:step]
#step+ve: forward direction :  begin to end-1
#step-ve: backward direction :  begin to end+1

l=[10,20,30,40,50]
print(l[2:7])    #[30, 40, 50]
print(l[2:7:2])  #[30, 50]
print(l[4:2])    #[]
print(l[8:2:-2])  #[50]
print(l[::1])    #[50, 40, 30, 20, 10]
print(l[::-1])   #[50, 40, 30, 20, 10]





