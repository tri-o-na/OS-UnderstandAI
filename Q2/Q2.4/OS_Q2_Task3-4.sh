#!/bin/bash
txtCount=0 # Initialize the current txt file count to 0

# Check through all files in the current directory, if the file ends with ".txt",
# increase txtCount by 1.
echo "All .txt Files in Current Directory: "
for entry in *
do

    if [[ $entry == *".txt" ]]; then
        txtCount=$(($txtCount+1))
        echo "$entry"
    fi
done
echo ""

# If the txtCount is greater than 0, there exist a .txt file in the directory to zip
# If txtCount reamins at 0, declare that there is no .txt file found in the directory and skip the zip process
if [ $txtCount -gt 0 ]; then
    echo "Zipping .txt files in current directory..."
    zip mytxt.zip *.txt # Zip all files in the current directory that ends with ".txt" to mytxt.zip file
    echo "Zip complete."
    echo ""
    # Print the current value of txtCount to indicate the number of .txt files found in the directory that was zipped
    echo "There are number of $txtCount .txt files and compressed into a .zip file" 
else
    echo "There are no .txt files found in the directory. No .zip file was made."
fi