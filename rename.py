import os

def rename_files(folder_path):
    for root, _, files in os.walk(folder_path):
        folder_name = os.path.basename(root)
        for file in files:
            file_path = os.path.join(root, file)
            new_file_name = f"{folder_name}_{file}"
            os.rename(file_path, os.path.join(root, new_file_name))

folder_path = '/Users/aaronnganm1/Documents/Zoom'
rename_files(folder_path)