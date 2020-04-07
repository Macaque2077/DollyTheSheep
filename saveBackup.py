from shutil import copy2
import os
import sys
import json

#backup a file by passing {original file location} {folder for copied file to be placed in}
#passed files are stored in a dictionary text file
def main(args):

    if len(args) > 0:
        file_loc = args[0]
        folder_name = args[1]
        savefile(file_loc, folder_name)
        writeJSON(file_loc, folder_name)

    else:
        saveExistingFiles()

    #copy the file
    # savefile(file_loc, folder_name)



    #write the files details to json
    # writeJSON(data, file_loc, folder_name)

def saveExistingFiles():
    try:
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for p in data['saves']:
                savefile(p['location'], p['folder'])
    except:
        print("no JSON saves found, you must pass a files location and the name of the folder you want store it in")
        
def savefile(file_loc, folder_name):
    
    file_name = file_loc.split("/")[-1]
    print(file_name)
    print(os.path.abspath(os.getcwd()))
    # could be improved to only check for the folder name in the location 
    saveslocation = "/home/machine/Desktop/backups"
    if not os.path.isdir("{}/{}".format(saveslocation,folder_name)):
        os.makedirs("{}/{}".format(saveslocation,folder_name))

    # checking if the file exists
    if os.path.isfile(str(file_loc)):
        print("found the file")
        copy2(file_loc, "{}/{}/{}".format(saveslocation,folder_name,file_name))

    else:
        print("are you sure {} exists?").format(str(file_loc))

def writeJSON(file_loc, folder_name):
    try:
        with open('data.txt') as json_file:
            data = json.load(json_file)
    except ValueError:
        print('no backups dictionary found, now creating one')
        data = {}
        data['saves'] = []

        
    data['saves'].append({
        'location' : str(file_loc),
        'folder' : str(folder_name)
        })

    with open('data.txt', 'w') as json_file:
        json.dump(data, json_file)
        

if __name__ == "__main__":
    main(sys.argv[1:])

