def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is not a Prime Number")


n = int(input("Enter a number: "))
prime_checker(n)