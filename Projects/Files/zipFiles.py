import zipfile
from pathlib import Path
import os
import shutil

compressZip = zipfile.ZipFile(Path.home() / Path('Desktop','New folder.zip'))

print(compressZip.namelist())

fileInfo = compressZip.getinfo('New folder/file_one.txt')

print(fileInfo.file_size)

print(fileInfo.compress_size)

# extract
os.chdir(Path.home() / Path('Desktop'))
compressZip.extractall()

compressZip.extract('New folder/file_one.txt', Path.home() / Path('Desktop','extractFile'))

# compress files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('New folder/file_one.txt')

# compress folder
folderZip = zipfile.ZipFile('newFolder.zip', 'w')
folderZip.write(Path.home() / Path('Desktop','New folder'))

shutil.make_archive("compressedFolder", 'zip', Path.home() / Path('Desktop','New folder'))