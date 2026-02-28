#WAP for folling requirment?
#i/p: aaabbbbzz
#o/p:  a3z2b4a3z2b4

s='aaabbbzzz'
output='' 
previous =s[0]
c=1
i=1
while i<len(s):
    if s[i] == previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
        if i ==len(s)-1:
            output=output+str(c)+previous
            i=i+1
print(output)

# s = 'aaabbbzzz'
# output = ''

# previous = s[0]
# count = 0

# for ch in s:
#     if ch == previous:
#         count += 1
#     else:
#         output += str(count) + previous
#         previous = ch
#         count = 1

# output += str(count) + previous

# print(output)
