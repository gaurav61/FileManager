import os
import shutil
from os import walk
def sort_files(path,sort_type):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        print(dirpath)
        files.extend(filenames)
        break
    if sort_type == 'ext':
        if path[-1]!='/':
            path = path + '/'
        extention_dict = {}
        for file in files:
            name,ext = os.path.splitext(file)
            if ext=='':
                key = 'file'
            else:
                key = ext[1:]
            if key in extention_dict:
                extention_dict[key].append(file)
            else:
                extention_dict[key] = []
                extention_dict[key].append(file)
        print(extention_dict)
        for key,value in extention_dict.items():
            if os.path.isdir(path+key):
                for file in value:
                    shutil.move(path+file,path+key+"/"+file)
            else:
                os.mkdir(path+key)
                for file in value:
                    shutil.move(path+file,path+key+"/"+file)