#string method:  count() to find no/- of occurances"
#counting substring in given string:
# s.count(substring)

s="ABBABBABA"  
print(s.count("B"))   #5
print(s.count("BB"))  #2
print(s.count("z"))   #0

print(s.count('B',4,100))  #3  Boundary

#ex2:
print("###############Exampe##########")
s="BBBBB"
print(s.count("B"))    #5
print(s.count("BB"))   #2
print(s.count("BBB"))  #1