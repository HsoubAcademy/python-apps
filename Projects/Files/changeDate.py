import shutil, os, re
from pathlib import Path

datePattern = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"

for filename in os.listdir(Path.home() / Path('Desktop','files')):
    search = re.search(datePattern, filename)

    if search == None:
        continue

    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)

    newFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print(f'Renaming "{filename}" to "{newFilename}"')

    oldName = Path.home() / Path('Desktop', 'files') / filename
    newName = Path.home() / Path('Desktop', 'files') / newFilename
    shutil.move(oldName, newName)