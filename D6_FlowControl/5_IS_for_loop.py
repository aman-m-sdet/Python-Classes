# Iterative Statements.:  For loop
# Repetative or multiole times:
# when i have to go for for loop:
# for x in sequence:          (list,set,tuple,dict,string,range)
        #activity

#Ex:1
S = "Sunny Lenon"
for ch in S:
    print(ch)

#Ex:2
w = 'Sunny lenon'
i=0
for s in w:
    print("The character {} index:{}".format(i,s))
    i=i+1  # or i+=1


# Dynamically need to read the Value:
S= input("Enter String: ")   # hello i am learing ython
for x in range(10):
    print(x)

for x in range(1,11):
    print(x)

#method 1:
for x in range(21):
    if x%2!=0:
        print(x)    # all odd number will print

#method 2:
for x in range(1,21,2):
    print(x)

# How to use for loop for list:
#to print sum of no/- givem list

numbers = list(map(int, input("Enter list of numbers: ").strip("[]").split(",")))
total = 0
for x in numbers:
    total += x
print("The sum is:", total)

