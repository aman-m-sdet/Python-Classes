#checking starting and ending part of a string
#1. s.startswith(substrings)
#2. s.endswith(substring)
#ex1:
s= "learning python is very easy"
print((s.startswith)('learning'))  #True
print(s.startswith('lea'))    #True
print(s.endswith("easy"))     #True
print(s.endswith("Easy"))    #False
print(s.endswith("sy"))      #True