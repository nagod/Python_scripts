import os
from tkinter import filedialog




def copyAllFiles():
    global path
    global array
    # get DirName
    filename = filedialog.askdirectory()
    path = filename
    
    #List of Files in Folder
    array = os.listdir(path)
        
def printRes(array):
    for file in array:
        print(file + "\n")

def getDublicates(array):

    #assume all files are lexicographically sorted
    for file in array:
        if
    lastAddedFile = ""

if __name__ == "__main__":
    
    #Saving the path and all files including this path
    path = ""
    array = []
    
    # Copy all files in array
    copyAllFiles()
    
    printRes(array)
    
    
