import os,sys
import shutil

#get the extension of a given file
def get_extension(filename):
    _,extension=os.path.splitext(filename)
    return extension

#create a new directory at given path
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)