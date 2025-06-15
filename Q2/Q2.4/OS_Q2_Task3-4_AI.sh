#!/bin/bash

# List all .txt files in current directory
txt_files=(*.txt)

# Check if any .txt files exist
if [ -e "${txt_files[0]}" ]; then
    count=${#txt_files[@]}

    # Compress all .txt files into mytxt.zip
    zip -q mytxt.zip "${txt_files[@]}"

    # Print summary message
    echo "There are $count .txt files and compressed into a .zip file"
else
    echo "There are 0 .txt files to compress"
fi
