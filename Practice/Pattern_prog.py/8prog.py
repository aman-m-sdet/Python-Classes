#To print inverted prymid pattern with * symbol
n = int(input("Enter no of rows:"))
for i in range(n):
    print((" "*i) + ("* "*(n-i)))

