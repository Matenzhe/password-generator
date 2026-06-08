import os
import shutil

# Change this to the folder you want to organize
folder_path = "C:/Users/thendoma/Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

# Create folders if they don’t exist
for category in file_types:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

# Move files into folders
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False

        for category, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, category, file))
                moved = True
                break

        if not moved:
            os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("✅ Files organized successfully!")