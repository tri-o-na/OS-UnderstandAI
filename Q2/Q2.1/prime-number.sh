#!/bin/bash

read -p "Give me a number: " number

if [ "$number" -eq 2 ]; then 
	echo "$number is a prime number"
elif [ "$number" -lt 2 ]; then
	echo "$number is not a prime number"
else
	for (( i=2; i*i<=number; i++ ))
	do 
		if (( number % i == 0 )); then
			echo "$number is not a prime number"
			exit
		fi
	done
	echo "$number is a prime number"
fi
