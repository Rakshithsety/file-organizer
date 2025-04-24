import os
import shutil

# Path of the folder you want to organize
folder_path = r"C:\Users\WELCOME\Downloads\testfolder" # Change this to your path of file which u want to organize

# Folder names and file extensions u can create ur own names for file name and give whichever type of file u want in it
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

# Create folders if not exist and no need if  already exist
for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# this is to move the files to their folders
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1].lower()
    file_moved = False

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            src = os.path.join(folder_path, filename)
            dest = os.path.join(folder_path, folder, filename)
            shutil.move(src, dest)
            file_moved = True
            break

# file which does not belong to respective folders u can shift it to others folder
    if not file_moved and os.path.isfile(os.path.join(folder_path, filename)):
        shutil.move(os.path.join(folder_path, filename),
                    os.path.join(folder_path, "Others", filename))

print("hurray,your files are organised in format prescribed by you")