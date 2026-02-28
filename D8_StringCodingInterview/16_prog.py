#WAP to find the no/- occurance of each character present in given string? with out using count.
# then use Dict  == {key : value} pair
s="aaaddddfggggggrrrrrrghhjjjj"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print("{} occurs {} items".format(k,v))
#for sorting
for k,v in sorted(d.items()):
    print("{} occurs {} items".format(k,v))