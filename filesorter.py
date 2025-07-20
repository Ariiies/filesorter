from dotenv import load_dotenv
import os
import shutil

load_dotenv()  # Loads variables from the .env file
my_path = os.getenv("PATH_TARGET")

# basic function to sort files by extension
def file_sorter(route: str):
    # for information purposes only
    folders_created = 0 
    files_moved = 0
    
    for file in os.listdir(route): 
        # create subdirectories based on the extensions of the files in a directory
        folder_path = os.path.join(route, os.path.splitext(file)[1][1:].capitalize())
        if not os.path.exists(folder_path):
            folders_created += 1
        os.makedirs(folder_path, exist_ok=True) 
        # move the files into their respective directories
        shutil.move(os.path.join(route, file), os.path.join(folder_path, file))
        files_moved += 1
    
    print(f"Folders created: {folders_created}, Files moved: {files_moved}")


file_sorter(my_path)

print("Done! ✅")

