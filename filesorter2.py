from dotenv import load_dotenv
import os, shutil

load_dotenv()  # Loads variables from the .env file
path = os.getenv("PATH_TARGET")

# reference
ref = {   "Photos": [".png", ".jpg", ".jpeg"],
          "Text": [".txt",".json",".html"],
          "Video":[".mov",".mp4",".wav",".avi"],
          "Docs":[".pdf",".docx",".dotx",".sql",".pptx",".csv",".xlsx"],
          "Audio":[".mp3",],
          "Executable":[".exe",] }

# basic function to sort files by extension 2
def file_sorter(path_target: str, reference: dict):
      print(f"Starting file classification in: {path_target}\n")
      
      # 1. Create destination directories
      all_extensions_in_dir = {os.path.splitext(file)[1].lower() for file in os.listdir(path_target) if os.path.isfile(os.path.join(path_target, file))}
      
      for category, extensions in reference.items():
            # Check if any of the category's extensions exist in the directory
            if any(ext in all_extensions_in_dir for ext in extensions):
                  category_path = os.path.join(path_target, category)
                  if not os.path.exists(category_path):
                        os.makedirs(category_path)
                        print(f"Directory created: '{category}'")

      # 2. Move files
      print("\nMoving files...")
      files_moved = 0
      for file in os.listdir(path_target):
            source_path = os.path.join(path_target, file)
            
            # Ensure it is a file and not a directory
            if os.path.isfile(source_path):
                  file_ext = os.path.splitext(file)[1].lower()
                  
                  for category, extensions in reference.items():
                        if file_ext in extensions:
                              destination_path = os.path.join(path_target, category, file)
                              shutil.move(source_path, destination_path)
                              print(f"-> File '{file}' moved to folder '{category}'")
                              files_moved += 1
                              break # Move to the next file once moved
      
      print(f"\nProcess completed. {files_moved} files were moved.")


file_sorter(path, ref)
print("Done! ✅")

