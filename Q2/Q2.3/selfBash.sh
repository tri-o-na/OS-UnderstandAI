#!/bin/bash

read -p "Enter integer numbers to key into list (seperate by 'space'): " -a numList
read -p "Enter a number: " target

found_pair=false

for ((i = 0; i < ${#numList[@]}; i++)); do
    for ((j = i + 1; j < ${#numList[@]}; j++)); do
        if [ $(( numList[i] + numList[j] )) -eq "$target" ]; then
            echo "The 2 numbers ${numList[i]} + ${numList[j]} sums to the keyed-in number $target"
            found_pair=true
        fi
    done
done

if [ "$found_pair" = false ]; then
    echo "There are no two numbers in the list summing to the keyed-in number $target"
fi