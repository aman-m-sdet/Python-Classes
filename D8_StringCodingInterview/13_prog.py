#WAP for following req?
#i/p: a4k3b2
#o/p: aeknbd
#in this ex folliong 2 func are used, 
#1. ord():  find unicode a=97
#2. chr(): corrsponding char fo given unicode


s="ak43b2"
output="" 
for ch in s:
    if ch.isalpha():
        x=ch
        output=output+ch
    else:
        d = int(ch)
        newc= chr(ord(x)+d)
        output=output+newc

print(output)