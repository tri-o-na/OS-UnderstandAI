#!/bin/bash

args=("$@") # Get all the argument as inputs in an array variable
largest=${args[0]} # Set the 1st item of the array to be the current largest
isError=0 # Set the error state of the program to default to 0. 0 = False, 1 = True

# Loop through the array. First check if the input is a number. If not, break out from the function with the the error state as true (isError=1)
# If input is a valid number, check if the current largest is smaller than input. If so, set the input to be the new largest
for i in "${!args[@]}"; do
    if [[ ! ${args[$i]} =~ ^[0-9]+$ ]]; then
        echo "Error: Unable to parse ${args[$i]} into a number."
        isError=1
        break
    fi
    
    if [ $largest -lt ${args[$i]} ]; then
    largest=${args[$i]}
    fi
done

# First check if there is any arguments, if not, print error for user to input arguments when running the program
# Then check if there was any error, if error state is true (isError=1), dont print the largest value and end the program
# If there isnt any error, print the largest number among the inputs
if [ -z "$1" ]; then
    echo "Error: Empty List. Please run program with arguments as inputs."
elif [ $isError -eq 1 ]; then
    echo "Program terminated."
else
    echo "$largest is the largest number."
fi