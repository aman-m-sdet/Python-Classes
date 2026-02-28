#Assume if you have string with alphabets and digits mixed, WAP to sort char of srt in first and digits next?
s=input("Enter only alphabets+digits:")
print(sorted(s))
# input : a1b2c3
#output: ['1', '2', '3', 'a', 'b', 'c']
#but need alphabets first

alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
print(alphabets)     #['a', 'b', 'c']
print(digits)        #['1', '2', '3']
output=''.join(sorted(alphabets)+sorted(digits))
print(output)     # abc123
