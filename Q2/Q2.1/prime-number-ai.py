# python code to check if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Request user input
number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(f"The keyed in number {number} is a prime number.")
else:
    print(f"The keyed in number {number} is not a prime number.")