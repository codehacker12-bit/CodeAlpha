import os
import shutil

def organize_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Get all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found in the folder to organize.")
        return

    # Organize files by their extensions
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_extension = file.split('.')[-1]

        # Create a folder for the file type if it doesn't exist
        extension_folder = os.path.join(folder_path, file_extension.upper())
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # Move the file to the respective folder
        shutil.move(file_path, os.path.join(extension_folder, file))

    print("Files have been organized successfully!")

if __name__ == "__main__":
    # Specify the folder path to organize
    folder_to_organize = input("Enter the folder path to organize: ")
    organize_folder(folder_to_organize)
