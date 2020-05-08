import time
import os
import shutil
from os import path

def main():
    count = 1
    while True:

        path = 'uploads'
        dest_path = 'uploadsMoved'

        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                files.append(os.path.join(r, file))

        # check if directory exists or not yet
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        for f in files:
            if os.path.exists(dest_path):
                # move files into created directory
                shutil.move(f, dest_path)
            print(f)

        print ("Python Server Alive ... ", count)
        count = count + 1
        time.sleep(7)
		
if __name__ == "__main__":
    main()