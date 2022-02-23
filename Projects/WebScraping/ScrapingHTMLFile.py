import bs4
from pathlib import Path

exampleFile = open(Path.home() / Path('Desktop','example.html'))
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))

elements = exampleSoup.select('p')
print(elements)
print(len(elements))
print(elements[0].getText())
print(elements[1].attrs)
