#1. Mathamatical operator:
print("############# Mathamatical operator ###############")
# -> + operator ---> for concatination
# -> * operator ---> for repetation

# string+string --> valid
# string*string --> invalid
# string+int --> invalid
# string*int --> valid

#Ex:1
print("Aman"+"Soft")  # both are string Amansoft
#print("aman"+0)   # type error
print("Aman"*3) # AmanAmanAman
print(3*"aman") # amanamanaman
#print(3.0*"aman") # error
#########################################################################################

#2. Membership operator:
print("############# Memebership operator ###############")
# -> "in" operator 
# -> "not in" operator

#'A' in 'Aman' -->True
#'Z' in 'Aman' -->Flase
#'Z' not in 'Aman' -->true

#Ex1:
s = input("enter main string:")
sub= input("enter sub string:")
if sub in s:
    print("sub string present in main string!!!")
else:
    print("sub string not present in main string!!!!")

##########################################################################################
#3. Comparision operator:
print("############# Comparision operator ###############")
# -> "<"    operator 
# -> "<="   operator
# -> ">"    operator 
# -> ">="   operator
# -> "=="   operator 
# -> "!="   operator

#unicode:
#'A'-65     'a'- 97
#'B'-66     'b'-98
#'C'-67     'c'-99
#'D'-68     'd'-100

#Ex1:
s1=input("enter first string:")
s2=input("enter second string:")
if s1==s2:
    print('Both are equal')
elif s1<s2:
    print("1st less than 2nd")
else:
    print("1st is greater than 2nd")