# Iterative Statements.
# To execute Group of statements:
#To execute group of statements based on condition..
# Syntax:  while cond:
                #body

#ex1:
i=1
while i<=5:
    print("Hello welocme to While loop")
    i =i+1          #print msg 5 times

#ex2:
i=1
while i<=5:
    print(i)
    i=i+1           #prints 1 2 3 4 5

#ex3:
#WAP to Print No's from 1-20 divisible by 3?
x=1
while x<=20:
    if x%3 == 0:
        print(x)      # 3 6 9 12 15 18
    x=x+1

#ex4:
#WAP to display sum of first n no's?      n = n(n+1)/2
n = int(input("Enter Number:"))
sum =0
i=1
while i<=n:
    sum =sum+i
    i=i+1
print("The Sum:", sum)    

#ex5:
#WAP
name =""
while name !="Sunny":
    name=input("Enter your fav Actor:")
print("Thanks for confirmation....")   # untill & unless Sunny is not match keep on ask to enter.