
#Selective Staement: Sample Example progams

#Q : WAP to find Biggest of 3 given No/-s:
x = int(input("Enter 1st Number (x):"))
y = int(input("Enter 2nd Number (y):"))
z = int(input("Enter 3rd Number (z):"))
if x>y and x>z:
    print("Biggest number is x",x)
elif y>z:
    print("Biggest number is y",y)
else:
    print("Biggest number is z",z)
