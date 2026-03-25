import urllib.request
from bs4 import BeautifulSoup


with open ("./seeds.txt", "r", encoding="UTF-8") as file:
    links = []
    for link in file:
        links.append(link)
        


text = ""



for link in links:
    print(link)
    page = urllib.request.urlopen(link)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    for img in soup.find_all('img'):
        imagem = img.attrs.get("src")
    
    text += f"<p>{title}</p> \n <img src={imagem} alt="">  \n"


message = f"""<html>
<head></head>
<body>{text}</body>
</html>"""


with open("index.html", "w", encoding="UTF-8") as file:
    file.write(message)
    

    
    