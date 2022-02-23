import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
#print(res.text)
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

element = noStarchSoup.select('#mp-tfa > p')
print(element)
print(element[0].getText())
