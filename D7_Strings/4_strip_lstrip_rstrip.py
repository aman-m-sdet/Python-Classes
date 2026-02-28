# String Metods:   Strip(), lStrip(), RStrip()
# Removing spoaces from the string:
#lStrip() ==> remove space lefthand side --> --xxxx
#rStrip() ==> remove space righthand side -->xxxx--
#Strip() ==> remove space begin & end side --> --xx--
#ex:1

#city= input("Enter city name:").lstrip()
#city = input("Enter city name:").rstrip()
city= input("Enter city name:").strip()
if city=="Hyd":
    print("Hello Hyderabad AADAB!!!!")
elif city == 'Chi':
    print("Hello Channai Vanakam!!!!")
elif city == 'Blr':
    print("Hello Bangalor Namaskara!!!")
else:
    print("You entered city is invalid????")