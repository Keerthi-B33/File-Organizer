import os
import shutil
import logging


logging.basicConfig(filename='organizer_info.log', level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s',filemode='w')

source_folder = input("Enter the path of source folder to organize: ").strip()

if not os.path.isdir(source_folder):
    print("Invalid source folder path.")
    exit()
       
destination_folder = input("Enter the path of  destination folder: ").strip()


if not os.path.isdir(destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    print(f"Created destination folder: {destination_folder}")

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx','.csv'],
    'Audio': ['.mp3', '.wav', '.mov'],
    'Archives': ['.zip', '.rar'],
    'Scripts': ['.py', '.js', '.html', '.css'],
}

def get_category(extension):
    for category, extensions in file_types.items():
        if extension in extensions:
            return category
    return 'Others'

def organize_files():
    try:
        for file in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file)
            if os.path.isfile(source_path):
                file, file_extension = os.path.splitext(file)
                file_extension = file_extension.lower()
                
                category = get_category(file_extension)
                category_folder = os.path.join(destination_folder, category)
                os.makedirs(category_folder, exist_ok=True)
                
                destination_path = os.path.join(category_folder, file)
                shutil.move(source_path, destination_path)
                print(f"{file} moved to {category}")
                logging.info(f"{file} moved to {category}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        logging.error(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error: {e}")
    finally:
        print("File organization completed.")



if __name__ == "__main__":
    organize_files()






