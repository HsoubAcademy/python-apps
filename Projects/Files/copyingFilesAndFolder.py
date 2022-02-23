import shutil
from pathlib import Path

shutil.copy(Path.home() / Path('Desktop','New folder','file_one.txt'), Path.home() / Path('Desktop','files','file_one_copied.txt'))
shutil.copytree(Path.home() / Path('Desktop','New folder'), Path.home() / Path('Desktop','folder backup'))