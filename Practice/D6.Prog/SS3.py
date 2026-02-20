#Selective Staement: Sample Example progams

#Q: WAP to check whether the given no/- is b/w 1 & 100:
n = int(input("Enter Number b/w '1 - 100' : "))
if n>=1 and n <100:
    print(" Given number is b/w '1 - 100'")
    print(" Given number {} is b/w '1 - 100'".format(n))
else:
    print("Given number is not in this range")
    print("Given number {} is not in this range".format(n))