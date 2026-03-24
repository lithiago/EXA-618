import requests
from bs4 import BeautifulSoup


with open ("./seeds.txt", "r", encoding="UTF-8") as file:
    links = []
    for line in file:
        links.append(line)
        
print(links)