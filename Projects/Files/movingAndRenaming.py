import shutil
from pathlib import Path

#shutil.move(Path.home() / Path('Desktop','New folder', 'test.txt'), Path.home() / Path('Desktop','files'))
#shutil.move(Path.home() / Path('Desktop','New folder', 'myFile.txt'), Path.home() / Path('Desktop','files', 'file.txt'))
#shutil.move(Path.home() / Path('Desktop','New folder', 'myFile.txt'), Path.home() / Path('Desktop','tests'))
#shutil.move(Path.home() / Path('Desktop','New folder', 'test.txt'), Path.home() / Path('Desktop','files'))
shutil.move(Path.home() / Path('Desktop','New folder', 'test.txt'), Path.home() / Path('Desktop','New folder', 'myFile.txt'))