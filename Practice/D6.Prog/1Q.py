#WAP to check whether the given no is prime or not
n = int(input("Enter the number: "))

if n <= 1:
    print("It is not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
