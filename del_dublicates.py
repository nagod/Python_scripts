import os
from PIL import Image
from PIL import ImageChops
from random import randrange
from progress.spinner import Spinner
def compareImages(img1, img2):
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        return False
    else:
        return True

if __name__ == "__main__":

    # Declaring Varis
    files = []  # Image, Filename, Filepath
    dublicates = []
    unwanted = []
    path = input("Please enter Folderpath. /PATH/TO/YOUR/FOLDER/ \n")
    folder_name = str(randrange(1000)) + "/"
    
    # Iterate through all files in directory and check wether its a file
    # Generate tmp Image and calc width/ height
    for file in os.listdir(path):
        if os.path.isfile(path + file):
            if ".DS_Store" in file:
                os.replace(path + file, "/Users/deniz/Desktop/"+file)
            elif "._" in file:
                unwanted.append(file)
            elif ".jpeg" or ".png" in file:
                tmp = Image.open(path + file)
                width, height = tmp.size
                files.append([tmp, file, path, width, height])

    # Declaring Processbar
    spinner = Spinner('Loading ')
    
    # Iterate trough all Images
    for counter in range(0, len(files)):
        for secondcounter in range(counter + 1, len(files)):
            # compare size of images
            if files[counter][3] == files[secondcounter][3] and files[counter][4] == files[secondcounter][4]:
                # compare Images and add dublicate to dublicate Array/List
                if compareImages(files[counter][0], files[secondcounter][0]):
                    if files[counter] not in dublicates:
                        dublicates.append(files[counter])
                    spinner.next()
        
    # Create Folder for Dublicates
    # !!!for Windows uncomment next line
    # os.chmod(path)
    dublicate_folder = path + folder_name
    os.mkdir(dublicate_folder)


    for f in dublicates:
        current_path = f[2] + f[1]
        new_path = dublicate_folder + f[1]
        os.replace(current_path, new_path)
