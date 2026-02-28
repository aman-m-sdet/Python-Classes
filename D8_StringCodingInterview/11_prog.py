#WAP for folling requirment?
#i/p: a3z2b4a3z2b4
#o/p: aaabbbbzz (sorted)

s=input("enter some string alph & digits:")
target=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d =int(ch)
        target= target+x*d
    output ="".join(sorted(target))
print(output)