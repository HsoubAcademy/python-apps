import os
from pathlib import Path
import shutil
import send2trash

#os.unlink(Path.home() / Path('Desktop','New folder', 'myFile.txt'))
#os.unlink(Path.home() / Path('Desktop','New folder'))
#os.rmdir(Path.home() / Path('Desktop','New folder', 'empty'))

#shutil.rmtree(Path.home() / Path('Desktop','New folder', 'myFolder'))

send2trash.send2trash(Path.home() / Path('Desktop','New folder', 'myFolder'))
send2trash.send2trash(Path.home() / Path('Desktop','New folder', 'myFile.txt'))