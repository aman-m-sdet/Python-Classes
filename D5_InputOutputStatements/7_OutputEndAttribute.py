#5. end attribute
print('hello')
print('durga')
print('software')

print('hello', end=' ')
print("durga", end=' ')
print('software')            #hello durga software

print('hello', end=':')
print("durga",end="***")
print("software")            #hello:durga***software

print(10,20,30, sep =":", end="***")
print(40,50,60, sep="!")          #10:20:30***40!50!60
print(70,80, sep="**",end="$$")    #70**80$$90 100
print(90,100)

print("Durga"+"Soft")    #DurgaSoft
print("Durga", "Soft")    #Durga Soft
print("##############################")