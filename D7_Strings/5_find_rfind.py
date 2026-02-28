#String Method: find() and rfind() to find the substring:
# finding Substring:
    #1. find()    ------->
    #2. rfind()   <------
    #3. index()
    #4. rindex()

# with out boundary
s="ABCCBA"
print(s.find('B'))   #1
print(s.find('Z'))   #-1
print(s.rfind("B"))   #4
print(s.rfind("z"))  #-1

print("#############Boundary############")
# boundary
# find(substring, begin,end-1)
# begin index to end-index
s='ABCDEFGHIJBK'
print(s.find("B"))    #1
print(s.find("B",3,8))  #-1
print(s.find("F",3,7))   #5
