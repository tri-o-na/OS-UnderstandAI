# find all pairs that add up to the targeted value
def check_all_sum_pairs():
    # Read list of integers from the user
    numbers = input("Enter a list of integers separated by spaces: ").split()
    numbers = list(map(int, numbers))

    # Read the target number
    target = int(input("Enter a number: "))

    found_pairs = []

    # Check all unique pairs
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                found_pairs.append((numbers[i], numbers[j]))

    # Output
    if found_pairs:
        print(f"These are the pairs summing to the keyed-in number {target}:")
        for a, b in found_pairs:
            print(f"{a} and {b}")
    else:
        print(f"There are no two numbers in the list summing to the keyed-in number {target}")

# Call the function
check_all_sum_pairs()