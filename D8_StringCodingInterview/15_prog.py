#WAP to find te number of occurance of each char present in given str with count() method and list[]:
s='AAAAAAAACVDDDDDDDDEEEEWWWWWWWWWWTEETTTYGDDDDDDDDDDDEEEEEEEEPPPPP'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
    for ch in sorted(l):
        print("{} occurs {} times".format(ch,s.count(ch)))
       # print("{} times '{}' occurs".format(s.count(ch),ch))
#method 2:

s = "AAAABBBBCCCC"
for ch in sorted(set(s)):
    print("{} occurs {} times".format(ch, s.count(ch)))