#method replace() tp perform replacement of one str with another str
#[s.replace(old str, new str)]

#ex1:
s="ABABAABA"
s1=s.replace("A", "B")
print(s1)    # BBBBBBBB

#ex2:
s= "Aman software solutions"
s1= s.replace(" ", '')
print(s1)
print("The no of space",s.count(''))

#replace () is case sensetive

#ex3:
s = "learning python is very difficult"
print(s.replace("difficult","easy"))
#print(s.replace("Difficult","easy"))  x