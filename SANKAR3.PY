import os
import shutil

source_folder = r'C:\Users\thota\OneDrive\Pictures'
destination_folder = r'C:\Users\thota\OneDrive'

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)