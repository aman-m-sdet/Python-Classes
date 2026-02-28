#* Python supports +ve and -ve indexing

s= "Aman"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
#print(s[-5])   #IndexError: string index out of range

#Ex1:
#WAP to display character of given string indexwise (both +ve & -ve)
word = input("Enter something like string:")
i=0
for chr in word:
    print("the char present at +ve index:{} and at -ve index{}".format(i,i-len(word),chr))
    i=i+1