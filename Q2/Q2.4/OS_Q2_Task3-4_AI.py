import os
import zipfile

def compress_txt_files():
    # Get list of .txt files in current directory
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and os.path.isfile(f)]
    
    count = len(txt_files)

    if count == 0:
        print("There are 0 .txt files to compress")
        return

    # Create a zip file and add all .txt files
    with zipfile.ZipFile('mytxt.zip', 'w') as zipf:
        for file in txt_files:
            zipf.write(file)

    print(f"There are {count} .txt files and compressed into a .zip file")

if __name__ == "__main__":
    compress_txt_files()
