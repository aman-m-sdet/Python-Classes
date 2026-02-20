#Transfer Statement: break statement
# to transfer control from one statement to another statement is called as TS
#1. break Statement:   2. continue Statement
# inside the loop if ypu want to break the cond you use break stmt
#ex1:
for i in range(10):
    if i ==7:
        print("Processing is enough")
        break
    print(i)
print("Outside the loop")

#ex2:
cart = [10,20,600,400]
for item in cart:
    if item >500:
        print("To place the order")
        break
    print("Processing item: ", item)

# if you want to use break or conitinue stmt 
# you should compulsory use with in for loop (or) while loop