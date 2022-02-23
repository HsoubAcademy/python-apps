from pathlib import Path

myFile = open('file_one.txt', 'w')
myFile = open(Path.home() / Path('Desktop','New folder','file_one.txt'), 'a')
myFile.write('\n16. Hello, how are you\n')
myFile.write('17. Hello, how are you\n')
myFile.write('18. Hello, how are you\n')

# writelines
# myList = ['\n14. Hello, how are you\n', '15. Hello, how are you\n']
# myFile.writelines(myList)