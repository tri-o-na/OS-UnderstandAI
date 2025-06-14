#!/bin/bash

read -p "Enter a number: " num

if [ "$num" -le 1 ]; then
    echo "The keyed in number $num is not a prime number"
    exit
fi

for (( i=2; i*i<=num; i++ ))
do
    if (( num % i == 0 )); then
        echo "The keyed in number $num not a prime number"
        exit
    fi
done

echo "The keyed in number $num is a prime number"
