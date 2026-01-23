#Byte & Byte Array -Group of bytes of array
# inbuilt function bytes
#################################################################################
l=[10,20,30]  #--> list
b=bytes(l)
print(type(b))  #<class 'bytes'>
for x in b:
    print(x)  # 10 20 30


# value only from (0 - 255)
# l=[10, 20,30,40,50,256]
# b=bytes(l)   # ValueError: bytes must be in range(0, 256)

# compulsury it is immutable(cannot change)
l=[20,30,40]
b = bytes(l)
print(b[0])   #20

# b[0]=77
# print(b)   #--> immutable cannot chnge the value
####################################################################

#Byte Array: (Mutable only this difference)
l =[10,20,30,40,50]
b=bytearray(l)
print(type(b))   #<class 'bytearray'>
print(b[0])      # 10
print(b[-1])     # 50

b[0] =77
for x in b:
    print(x)  # 77 20 30 40 50