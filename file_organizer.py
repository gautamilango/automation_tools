import os, sys, shutil
from pathlib import Path


main_dir = os.getcwd()
dataset_name = sys.argv[1]
dataset_dir = main_dir / Path(dataset_name)
sorted_dir = main_dir / Path(dataset_name + "_SORTED")

# Change my directory to the directory that holds all the files
os.chdir(dataset_dir)

print("Sorting started ...")

file_types = set()
folder_names = list()

for f in os.listdir():
    _, file_ext = os.path.splitext(f)
    file_types.add(file_ext)

 # Ignore hidden files such as .DStore
if "" in file_types:
    file_types.remove("")

for file_type in file_types:
    folder_names.append(file_type.replace(".", ""))

os.makedirs(sorted_dir, exist_ok=True)
os.chdir(sorted_dir)

for folder_name in folder_names:
    os.makedirs(folder_name.upper(), exist_ok=True)

os.chdir(dataset_dir)

for f in os.listdir():
    _, file_ext = os.path.splitext(f)
    f = Path(f)
    shutil.copy(dataset_dir / f, sorted_dir / Path(file_ext.replace(".", "") / f))


print("Finished sorting")
