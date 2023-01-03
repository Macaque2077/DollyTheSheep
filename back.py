import os
from os.path import isdir, join
import csv
from pathlib import Path
from distutils.dir_util import copy_tree

from time import time, ctime

def get_time():
    now = ctime().split()
    date = [now[2], now[1], now[-1]]
    date.extend(now[3].split(":")[:2])
    return "-".join(date)

file_path = "file_names.csv"
backup_path = "backups"

def backup(row):
    save_time = get_time()
    out_path = os.path.join(backup_path, row[0])
    copy_tree(row[1], join(out_path, save_time))

def read_backfile():
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",") 
        for row in reader:
            backup(row)

def manage_saves():
    fu = [f.path for f in os.scandir(backup_path) if f.is_dir()]
    for path in fu:
        print(path)        

if __name__ =="__main__":
    # read_backfile()
    manage_saves()
