#WAP to reverse order of wordspresent in string?

s="Learning python is very easy"
l=s.split()
print(l)      #['Learning', 'python', 'is', 'very', 'easy']
l1=l[::-1]
print(l1)     #['easy', 'very', 'is', 'python', 'Learning']
output = " ".join(l1)
print(output)  #easy very is python Learning