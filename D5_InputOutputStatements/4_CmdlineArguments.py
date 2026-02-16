#command line arguments  py test.py 10 20 30
# sys --> predefine module
# argv ---> arguments present in sys module

#Demo5: prog: command line arugments:
#another way to read the user ip we run in cmd prompt.

##############################################################
from sys import argv
print(type(argv))
print(argv[1])

#Demo1: Prog1 Print cmd line informaion
# Run in cmd line:--> python .\4_CmdlineArguments.py 10 20 30 40
from sys import argv
print("The number of cmd line arg :", len(argv))
print("The list of cmd line argv :", argv)
print("The cmd list arg one by one:")
for x in argv:
    print(x)


#Demo2 : prog2: Print sum of 2 num in cmdline arg:
from sys import argv
args = argv[1:]
sum=0
for v in args:
    sum =sum + int(v)
print("The sum is:", sum) 

#WHERE WE USE THIS CMDLINE IN PERFECT USE: file manage app
# i have 2 file i need to merge
# HARD CODED
f1=open("a.txt")   # only R Read access
f2=open("b.txt")   # only R Read access
f3=open("c.txt",'w')   # write in F3
for l in f1:
    f3.write(l)

for l in f2:
    f3.write(l)

#DYNAMICALLY 
f1 = open(argv[1])
f2 = open(argv[2])
f3 = open(argv[3],'W')
for ln in f1:
    f3.write(ln)
for ln in f2:
    f3.write(ln)
#python test.py a.txt b.txt c.txt    

#########################################
#Imp concuusion about cmd line argv is:
#case1:
from sys import argv
print(argv[1])
#py test.py "Aman Anju"

#case2:
from sys import argv
print(argv[1]+argv[2])    #1020
print(int(argv[1])+int(argv[2]))   #30
#py test.py 10 20

#case3:
from sys import argv
print(argv[100])
#py test.py 10 20   # index error out of range