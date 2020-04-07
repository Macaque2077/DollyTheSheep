from shutil import copy2
import os
import sys

#backup a file by passing {original file location} {folder for copied file}
def main(args):
    file_loc = args[0]
    folder_name = args[1]

    file_name = file_loc.split("/")[-1]
    print(file_name)
    print(os.path.abspath(os.getcwd()))

    saveslocation = "/home/machine/Desktop/backups"
    if not os.path.isdir("{}/{}".format(saveslocation,folder_name)):
        os.makedirs("{}/{}".format(saveslocation,folder_name))

    if os.path.isfile(str(file_loc)):
        print("found the file")
        copy2(file_loc, "{}/{}/{}".format(saveslocation,folder_name,file_name))

    else:
        print("are you sure this file exists?")
    

if __name__ == "__main__":
    main(sys.argv[1:])

