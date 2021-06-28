import os
import shutil

source = input("Enter source folder name: ")
destination = input("Enter destination folder name: ")

source = source + '/'
destination = destination + '/'

listOfFiles = os.listdir(source)
print(listOfFiles)

for file in listOfFiles:
    shutil.move((source + file), destination)