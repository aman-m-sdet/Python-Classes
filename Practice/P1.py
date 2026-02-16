input = "This is python Testing"
#output = "siht is nohtyp gnitseT"

#Type1: Split Entair Line
print(input[::-1])          #gnitseT nohtyp si sihT

#Type2:   Split each word and reverse
words = input.split()
reversed_words = [word[::-1] for word in words]
output = " ".join(reversed_words)

print(output)                #sihT si nohtyp gnitseT

#Type3: Split 1 after other wrd 
input1 = "Aman Anjum"
w1, w2 = input1.split()

print(w1[::-1], w2)          # Type 1      namA Anjum
print(w1, w2[::-1])          # Type 2      Aman mujnA
print(w1[::-1], w2[::-1])    # Type 3 namA mujnA

#Type4: Split 1 after other wrd 
s = "Aman Anjum"
def reverse_one_word(s, reverse_first=True):
    w1, w2 = s.split()
    if reverse_first:
        return w1[::-1] + " " + w2
    else:
        return w1 + " " + w2[::-1]

print(reverse_one_word(s, True))     # namA Anjum
print(reverse_one_word(s, False))    # Aman mujnA


#type5:
input_str = "This is python Testing"
reverse_words = {"This", "Testing"}  # words to reverse

result = []
for word in input_str.split():
    if word in reverse_words:
        result.append(word[::-1])
    else:
        result.append(word)

output = " ".join(result)
print(output)                       #sihT is python gnitseT

#type5.1:    Short & clean version
input_str = "This is python Testing"
reverse_words = {"This", "Testing"}

print(" ".join(
    word[::-1] if word in reverse_words else word
    for word in input_str.split()
))                                   #sihT is python gnitseT

# P
S = "This is Python Testing Classes"
Reverse_words = {"This" ,"Python", "Classes"}
print(" ".join(
    word[::-1] if word in Reverse_words else word
    for word in S.split()
))                                   #sihT is nohtyP Testing sessalC
