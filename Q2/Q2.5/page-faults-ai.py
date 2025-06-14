def fifo_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0
    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)  # Remove the oldest page
                memory.append(page)
    return page_faults

def main():
    # Input number of frames (3 to 6)
    while True:
        try:
            frames = int(input("Enter number of frames (3-6): "))
            if 3 <= frames <= 6:
                break
            else:
                print("Please enter a number between 3 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Input reference string length (15 to 25)
    while True:
        ref_string_input = input("Enter reference string of page numbers separated by commas (length 15-25): ")
        try:
            reference_string = [int(x.strip()) for x in ref_string_input.split(',')]
            if 15 <= len(reference_string) <= 25:
                break
            else:
                print("Please enter between 15 and 25 page numbers.")
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

    page_faults = fifo_page_replacement(frames, reference_string)
    print(f"Total number of page faults: {page_faults}")

if __name__ == "__main__":
    main()
