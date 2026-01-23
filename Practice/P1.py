input = "This is python Testing"
#output = "siht is nohtyp gnitseT"


words = input.split()
reversed_words = [word[::-1] for word in words]
output = " ".join(reversed_words)

print(output)

#print(" ".join(word[::-1] for word in input.split()))

# input1= "Aman Anjum"
# print(input1[0::-1].split())

