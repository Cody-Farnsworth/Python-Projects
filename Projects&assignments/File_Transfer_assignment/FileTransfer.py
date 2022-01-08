import shutil
import os

source = '/Users/coffe/OneDrive/Documents/GitHub/Python-Projects/Projects&assignments/File_Transfer_assignment/Folder A/'

destination = '/Users/coffe/OneDrive/Documents/GitHub/Python-Projects/Projects&assignments/File_Transfer_assignment/Folder B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
