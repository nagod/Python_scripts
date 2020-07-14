import os
import shutil
import schedule


def delete_downloads():
    text = " This is a Py Scheduler. 
    print(text)
    current_dir = os.getcwd()
    expected_dir = input("Please enter Folderpath. /PATH/TO/YOUR/FOLDER/ \n")
    print(os.getcwd())
    if current_dir != expected_dir:
        os.chdir(expected_dir)

    for file in os.listdir():
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
    return

schedule.every(15).seconds.do(#Enter your TASK!)

while True:
    schedule.run_pending()
