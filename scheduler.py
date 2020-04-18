import os
import shutil
import schedule


def delete_downloads():
    current_dir = os.getcwd()
    expected_dir = "/Users/deniz/Downloads"
    print(os.getcwd())
    if current_dir != expected_dir:
        os.chdir(expected_dir)

    for file in os.listdir():
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
    return


schedule.every(15).seconds.do(delete_downloads)

while True:
    schedule.run_pending()
