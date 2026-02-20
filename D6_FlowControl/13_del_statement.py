#delete variable
# del in keyword in python
# x=10
# del x
# print (x)

#Ex2:
s1 = "Murga"
s2=s1
s3=s2
del s1
print(s2,s3)  # o/p Murga Murga
del s2,s3

#ex3:
s = "aman"
del s[0]  # you cannot delete or change error

#Del Statement
#1. del is a keyword in python
#2. we can use del to delete variable
#3. the main advantage of del is we can make objects eligible for garbage collection
# so that memory will be improved
