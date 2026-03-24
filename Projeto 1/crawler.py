import requests


URL =  "https://www.imdb.com/pt/chart/top/"

response = requests.get(URL)

# data = response.json()

print(response.text)