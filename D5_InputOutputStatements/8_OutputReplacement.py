#6. print object with replacement operator
print(object)
l=[10,20,30,40]
print(l)      #[10, 20, 30, 40]

t=(10,20,30,40)
print(t)     #(10, 20, 30, 40)

#print Statement with replacement operator   "{}"
name ="durga"
sal =20000
fr ="matha"

#Output:    hello durga, your salary is 20000, and your friend matha waiting
print('hello {}, your salary is {}, and your friend {} waiting'.format(name,sal,fr))
print('hello {0}, your salary is {1}, and your friend {2} waiting'.format(name,sal,fr))
print('hello {n}, your salary is {s}, and your friend {f} waiting'.format(n=name,s=sal,f=fr))

#example2:
a,b,c,d =10,20,30,40
print('a={},b={},c={},d={}'.format (a,b,c,d))  #a=10,b=20,c=30,d=40

