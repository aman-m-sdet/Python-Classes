#WAP for folling requirment?
#input: a4b2c3
#output: aaaabbccc
s = input("type: a4b2c3 : ")
output = ""

for ch in s:
    if ch.isalpha():
        x = ch          # store character
    else:
        d = int(ch)     # convert digit
        output = output + (x * d)

print(output)

