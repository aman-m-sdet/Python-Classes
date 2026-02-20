#Digit to word conversion prog:

#WAP to take a single digit no/- from keyboard & print itd value in english:
# 1st method:
n = int(input("Enter Any Digit from '0-9': "))
if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Entered Number {} = Five".format(n))
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
elif n == 10:
    print("Ten")
else:
    print("Enter only form 0-9")

# 2nd method:

list = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
num= int(input("Enter Digit from 0-9: "))
print(list[num])