from os import listdir
from os.path import isfile, join
import re
import os

path = "/mnt/c/Utils"

for dir_item in listdir(path):
    dir_item_with_path = join(path, dir_item)
    if isfile(dir_item_with_path):
        print(dir_item)
        match = re.search(r"🚘(.+) \((\d+)", dir_item)
        if match == None:
            print('ERROR! Regex did not found anything')
        else:
            series_num = match.group(2).zfill(2)
            series_name = match.group(1)

            new_filename = f"{series_num} {series_name}.mp4"
            print(new_filename)

            new_filename_with_path = join(path, new_filename)

            os.rename(dir_item_with_path, new_filename_with_path)
        
