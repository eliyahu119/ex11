import zipfile
import os

def create_zip(files, folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                zipf.write(file_path, arcname=file)

# Example usage
files =['boggle_logic.py', 'boggle.py', 'count_down_timer.py', 'end_screen.py',
        'ex11_utils.py', 'gui.py',"open_screen.py ","path.py"
  ,'boggle_dict.txt', 'boggle_board_randomizer.py',"AUTHORS"]
# Example usage
current_folder = os.getcwd()  # Get the current working directory
zip_name = os.path.join(current_folder, 'ex11.zip')

create_zip(files, current_folder, zip_name)
