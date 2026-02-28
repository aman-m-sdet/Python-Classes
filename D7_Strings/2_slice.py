#slice Operator:
# Slice means Substring
# index means only 1 char
#Syntax :  $ [begin:end]
#Syntax : S[begin : end : step]
#-substring from [begin] index to [end-1] index
#begin is optional & defaule valus is 0
#end is optional & default value is len(s)
########################################################

#Syntax :  $ [begin:end]
print("############'begin:end - slice operator'############")
s ="abcdefghijk"
print(s[2:7])
print(s[:7])
print(s[2:])
print(s[:7])
print(s[:])
print(s[:-7])
print(s[-2:])

# Syntax : S[begin : end : step]
print("############'Step'############")

s ="abcdefghijk"
print(s[2:7])
print(s[2:7:1])
print(s[2:7:2])
print(s[2:7:3])
print(s[::2])
print(s[::3])
print(s[::-1])

# Slice Operator Case study
print("############'Slice Operator Case study'############")

s="abcdefghij"
print(s[:])     #abcdefghij
print(s[1:6:2]) #bdf
print(s[::1])   #abcdefghij
print(s[::-1])  #jihgfedcba
print(s[3:7:-1]) #empty
print(s[7:4:-1]) #hgf
print(s[1:6:2]) #bdf
print(s[0:1000:1]) #abcdefghij
print(s[-4:1:-1])   #gfedc
print(s[-4:1:-2])   #gec
print(s[5:0:1])   #empty
#print(s[9:0:0])   # error step cannot be zero
print(s[0:-10:-1]) #empty
print(s[0:-11:-1])#empty
print(s[0:0:1])  # a
print(s[0:-9:-2])#empty
print(s[-5:-9:-2])#empty
print(s[10:-1:-1])# fd
print(s[1000:2:1])# empty