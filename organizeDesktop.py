import os
import shutil
from datetime import datetime

def organize():
    today = datetime.today().strftime('%Y-%m-%d')

    desktop_path = os.path.expanduser('~/Desktop')
    documents_path = os.path.expanduser('~/Documents')

    folder_path = os.path.join(documents_path, today)
    os.makedirs(folder_path, exist_ok=True)

    for item_name in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item_name)
        if os.path.isfile(item_path) or os.path.isdir(item_path):
            shutil.move(item_path, folder_path)
            print(f"Moved {item_name} to {folder_path}")

if __name__ == "__main__":
    organize()   
