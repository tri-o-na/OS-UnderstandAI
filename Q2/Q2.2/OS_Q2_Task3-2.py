import sys

def printLargestNumber(input):
    if not input: #Print error when there is no input and return from the function.
        print("Error: Empty List. Please run program with arguments as inputs.")
        return
    
    listOfNum = []

    #Parse input into float. If fail return from the function.
    for x in input:
        try:
            listOfNum.append((float(x)))
        except Exception as e:
            print("Error:",e)
            return

    # After parsing all inputs, set the first number of the list to be the current largest
    currentLargest = listOfNum[0]

    # Check through the list and get the largest value
    for x in listOfNum:
        if currentLargest < x:
            currentLargest = x

    # Print largest value
    print(currentLargest,"is the largest number.")

printLargestNumber(sys.argv[1:])