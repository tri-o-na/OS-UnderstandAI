#!/bin/bash

# Check if at least one number is provided
if [ "$#" -eq 0 ]; then
  echo "Usage: $0 number1 number2 ... numberN"
  exit 1
fi

# Initialize largest with the first number
largest=$1

# Loop through all arguments
for num in "$@"; do
  if (( num > largest )); then
    largest=$num
  fi
done

echo "$largest is the largest number"
