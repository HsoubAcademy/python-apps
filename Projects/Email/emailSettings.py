import ezgmail, os
from pathlib import Path

os.chdir(Path.home() / Path('Desktop', 'Projects', 'emails'))
ezgmail.init()
