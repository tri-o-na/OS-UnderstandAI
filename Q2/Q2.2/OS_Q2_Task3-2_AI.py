import sys

def find_largest(numbers):
    if not numbers:
        print("No numbers provided.")
        return

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    print(f"{largest} is the largest number")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_largest.py num1 num2 ... numN")
    else:
        try:
            # Convert arguments (strings) to integers
            input_numbers = list(map(int, sys.argv[1:]))
            find_largest(input_numbers)
        except ValueError:
            print("Please provide only integer numbers.")
