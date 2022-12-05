import pathlib
from pathlib import Path

file_path = pathlib.Path("/my_folder/my_file.txt")
file_path =Path.cwd()/"my_folder"
file_path.mkdir(exist_ok=True)
new_file_path = file_path/"my_file.txt"
new_file_path.touch(exist_ok=True)
print(file_path.exists())
print(new_file_path.name)
print(file_path.name)