import pathlib
from pathlib import Path

path_1 = pathlib.Path.home()
folder_1 = path_1 / "PycharmProjects" / "semicolonPythonProjects" / "pratice" / "my_folder1"
folder_1.mkdir(exist_ok=True)

files = [folder_1 / "file1.txt",
         folder_1 / "file2.txt",
         folder_1 / "image.png"]

for path in files:
    path.touch()
folder_2 = path_1 / "PycharmProjects" / "semicolonPythonProjects" / "pratice" / "my_folder1" / "images"
folder_2.mkdir(exist_ok=True)
print(folder_2.exists())
source = path_1 / "PycharmProjects" / "semicolonPythonProjects" / "pratice" / "my_folder1" / "image.png"
print(source.exists())
destination = path_1 / "PycharmProjects" / "semicolonPythonProjects" / "pratice" / "my_folder1" / "images" / "image.png"
print(destination.exists())
source.replace(destination)
rm_file = folder_1 / "file1.txt"
rm_file.unlink()
print(rm_file.exists())
# folder_1.rmdir()
# print(folder_1.exists())
