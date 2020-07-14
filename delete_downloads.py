import os
import shutil


current_dir = os.getcwd()
expected_dir = input("Please enter Folderpath. /PATH/TO/YOUR/FOLDER/ \n")

print(os.getcwd())
if current_dir != expected_dir:
    os.chdir(expected_dir)

test = input("Willst du alle dateien löschen ?? [Y]ES or [N]O \n")

if test == "Y" or "y":
    for file in os.listdir():
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
else:
    print(":(")
