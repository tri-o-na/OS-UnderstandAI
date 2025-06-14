def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: #check if number divisible by any number other than 1 and itself
            return False
    return True

n = int(input("Give me a number: "))
if prime(n):
    print(f"the key in number {n} is a prime number.")
else: 
    print(f"the key in number {n} is not a prime number.")