#WAP for following requirment?
#i/p: ABAABBCA
#o/p: 4A3B1C

s= "ABAABBCA"
output=""
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output=output+str(v)+k
print(output)


#WAP for following requirment?
#i/p: ABAABBCA
#o/p: A4B3C1
s= "ABAABBCA"
output=""
d={}
for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    output=output+k+str(v)
print(output)