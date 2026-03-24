import urllib.request
from bs4 import BeautifulSoup


with open ("./seeds.txt", "r", encoding="UTF-8") as file:
    links = file.read()
        

page = urllib.request.urlopen("")    