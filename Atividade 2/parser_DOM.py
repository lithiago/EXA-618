import time
from xml.dom.minidom import parse
import csv

# from xml.dom.minidom import parse

# BancoDocument = parse('Banco.xml')

# print("Starting DOM Parser...")
# for c in BancoDocument.getElementsByTagName("Cliente"):	
# 	print("Nome:", c.getElementsByTagName("nome")[0].firstChild.data)
# 	print("id: ", c.getAttribute("id"))



VenezaDocument = parse("map_veneza.osm")
# Definindo os campos
dados = []
latitude = ""
longitude = ""
tipo = ""
nome = ""
id = ""

inicio = time.time()
for node in VenezaDocument.getElementsByTagName("node"):
    latitude = node.getAttribute('lat')
    longitude = node.getAttribute('lon')
    id = node.getAttribute('id')
    
    for c in node.getElementsByTagName('tag'):
        key = c.getAttribute('k')
        if key == 'name':
            nome = c.getAttribute('v')
        elif key == 'amenity':
            tipo = c.getAttribute('v')
    if nome and tipo:
        dados.append({
            'id': id,
            'Latitude': latitude,
            'Longitude': longitude,
            'Tipo': tipo,
            'Nome': nome
        })
    latitude = ""
    longitude = ""
    tipo = ""
    nome = ""
    id = ""

                
fim = time.time()

print(f"Tempo total: {fim - inicio}")       
with open('./DOM_PARSER.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'Latitude', 'Longitude', "Tipo", 'Nome'])
    writer.writeheader()
    writer.writerows(dados)
