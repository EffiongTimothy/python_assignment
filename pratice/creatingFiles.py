import pathlib

path = pathlib.Path.cwd()
first_folder = path / "Practice"
first_folder.mkdir()
print(first_folder.exists())
sub_folder1 = first_folder / "document"
sub_folder1.mkdir()
print(sub_folder1.exists())
sub_folder2 = first_folder / "image"
sub_folder2.mkdir()
print(sub_folder2.exists())
files_folder = [sub_folder2 / "image1.png",
                sub_folder2 / "image2.gif",
                sub_folder2 / "image3.png",
                sub_folder2 / "image4.jpg"]
for files in files_folder:
    files.touch()
    print(files.exists())
#
# file1 = first_folder / "image1.png"
# source = path / first_folder / file1
# print(source.exists())
# destination = path / first_folder /" image"/ "image1.png"
# print(destination.exists())
# source.replace(destination)
