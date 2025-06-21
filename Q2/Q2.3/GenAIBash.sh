#!/bin/bash

# Read list of integers from the user
read -p "Enter a list of integers separated by spaces: " -a numbers

# Read the target number
read -p "Enter a number: " target

found=false
length=${#numbers[@]}

# Check all pairs
for (( i=0; i<length; i++ )); do
    for (( j=i+1; j<length; j++ )); do
        sum=$(( numbers[i] + numbers[j] ))
        if [ "$sum" -eq "$target" ]; then
            echo "Pair: ${numbers[i]} and ${numbers[j]}"
            found=true
        fi
    done
done

# Final output
if [ "$found" = true ]; then
    echo "These are the pairs summing to the keyed-in number $target"
else
    echo "There are no two numbers in the list summing to the keyed-in number $target"
fi
