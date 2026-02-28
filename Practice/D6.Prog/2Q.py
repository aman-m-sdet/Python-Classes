#WAP To generate prie num which are less than or equal to given num?

n = int(input("Enter any number: "))

n1 = 2
while n1 < n:
    is_prime = True
    #for i in range(2,n1/2+1):
    for i in range(2, int(n1**0.5) + 1):
        if n1 % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n1)

    n1=n1+1