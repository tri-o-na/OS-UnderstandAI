# making user input split by space and storing into list
numbers = [int(i) for i in input("Enter a list of integers separated by spaces: ").split()] 
target = int(input("Enter a number: "))

found = False

# comparing 2 items in list
for i in range(len(numbers)): 
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"The 2 numbers {numbers[i]} + {numbers[j]} sum to {target}")
            found = True

if not found:
    print(f"There are no two numbers in the list summing to the keyed-in number {target}")

    