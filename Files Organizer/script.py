import os, shutil, sys

self_name = sys.argv[0].split('\\')[-1]     # To get the script's name

for file_name in os.listdir():
    if file_name == self_name:              # Skip; to avoid moving the running script
        continue
    if os.path.isdir(file_name):            # Don't move folders into folders
        continue

    if '.' in file_name:                    # Files with Extention
        ext = file_name.split('.')[-1].lower()
        folder_name = ext + " files_"
    else:                                   # Files without Extention
        folder_name = "no extension files_"

    if not os.path.exists(folder_name):     # Create required folder if necessary
        os.makedirs(folder_name)

    try:
        shutil.move(file_name, folder_name) # Move file into the destination folder
    except shutil.Error:
        print("Error moving file " + file_name)

print("Successfully Executed.")
