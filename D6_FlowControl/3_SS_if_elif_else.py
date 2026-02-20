##Selection Statement:  IF-elif-Else Statement:
# - {colon & intendation is mndatory}
# syntax: if cond 1:
                #Action 1
            #elif cond 2:
                #Action 2
            #elif cond 3:
                #Action 3
            #.
            #.
            #else:    # thi is optional
                #Default action

#ex:1
brand = input("Enter your Fav Car brand: ")
if brand == 'MS':
    print("it is Maruthi Suzuki")
elif brand == 'TM':
    print("It is TATA Motors") 
elif brand == "KM":
    print("This is Kia Motors")  
elif brand == 'HM':
    print("This is Honda Motors")
else:
    print("Car Brand is not found, it might be other new brand.....")

# if cond met if part will print
# if cond doesnot met only else part will print.
# here else: Is Optional.