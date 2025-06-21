#!/bin/bash

# input user prompt 
read -p "Enter integer numbers to key into list (seperate by 'space'): " -a numList #saved to variable array 'numList'
read -p "Enter a number: " target #saved to variable 'target'

found_pair=false

#for loop to compare 2 values
for ((i = 0; i < ${#numList[@]}; i++)); do
    for ((j = i + 1; j < ${#numList[@]}; j++)); do
        if [ $(( numList[i] + numList[j] )) -eq "$target" ]; then  # compare the 2 values
            echo "The 2 numbers ${numList[i]} + ${numList[j]} sums to the keyed-in number $target"
            found_pair=true #boolean true
        fi
    done
done

if [ "$found_pair" = false ]; then  # boolean false then print output
    echo "There are no two numbers in the list summing to the keyed-in number $target"
fi