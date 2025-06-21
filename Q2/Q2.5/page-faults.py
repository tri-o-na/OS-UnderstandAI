# example reference string
# ref = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
# frameNum = 3  # number of frames

# frameNum = int(input("Key in the number of available frames in memory at a time from 3 to 6: "))
# ref_input = input("Key in the reference string of referenced page numbers from 15 to 25: ")
# ref = [int(x.strip()) for x in ref_input.split(',')]


frameList = []  # list to hold the frames

def pageFaults(ref, frameNum, frameList):
    counter = 0 # page faults counter
    for i in ref: 
        if i not in frameList:
            frameList.append(i) # add the page to frameList if not already inside
            counter += 1 # increase page faults count
            if len(frameList) > frameNum:
                frameList.pop(0) # if frameList exceeds frameNum, pop from the top
        frameStr = ', '.join(str(x) for x in frameList)
        print(f"{i}\t{frameStr}")
    print("Total Number of Page Faults: " + str(counter))

def main():
    while True:
        try: 
            frameNum = int(input("Key in the number of available frames in memory at a time from 3 to 6: "))
            if frameNum < 3 or frameNum > 6:
                print("Please enter a number between 3 and 6 for the number of frames.")
            else:
                break
        except ValueError:
            print("Invalid. Please enter an integer.")
    
    while True:
        try:
            ref_input = input("Key in the reference string of referenced page numbers from 15 to 25 (comma separated): ")
            ref = [int(x.strip()) for x in ref_input.split(',')]
            if len(ref) < 15 or len(ref) > 25:
                print("Please enter a reference string with length between 15 and 25.")
            else:
                break
        except ValueError:
            print("Invalid. Please enter an integer.")
    print("\nPage\tFrame\t")
    print("-" * 20)
    pageFaults(ref, frameNum, frameList)

if __name__ == "__main__":
    main()


'''
Thought process:
- get inputs for frameNum and ref
- add the page to frameList (if num not alr inside, if inside, go next page) -> increase count
    -> make sure the frameList dun exceed frameNum
        -> if exceed then pop from top, add in bottom -> increase count
'''