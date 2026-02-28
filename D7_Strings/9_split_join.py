#String method: split() and join() str
# i want to split string using seperator -- default is space
#ex1:
s = " Aman Sofware solutions" 
l = s.split()
print(l)     #['Aman', 'Sofware', 'solutions']
for x in l:
    print(x)

print("##########EX2###########")
#ex2:
d= "21-02-2026"
l = d.split("-")
print(l)
for x in l:
    print(x)

print("##########Join of strings###########")
l=("aman","software","solutions")
#syntax: sperator.join(l)
s="*".join(l)
print(s)       #aman*software*solutions