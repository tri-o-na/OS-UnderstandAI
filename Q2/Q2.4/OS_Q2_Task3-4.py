import os
import zipfile

dir_list = os.listdir() # Get all files in the current directory
txtFiles = [] # Initialize an empty list to store all .txt files

# Filter through the files in the current directory to find only .txt files and add to the txtFiles list
print("All .txt Files in Current Directory:")
for file in dir_list:
    if file.endswith(".txt"):
        txtFiles.append(file)
        print(file)

print()
# If there exist a .txt file in the directory, proceed with the zipping process
if (len(txtFiles) > 0):
    zip = zipfile.ZipFile("mytxt.zip", "w", zipfile.ZIP_DEFLATED) # Create the zip file
    for file in txtFiles:
        zip.write(file) # Add the .txt files to the zip file
    zip.close()
    print(f"There are number of {len(txtFiles)} .txt files and compressed into a .zip file")
# If there isnt, declare that there was no .txt files found in the current directory
else:
    print("There are no .txt files found in the directory. No .zip file was made.")