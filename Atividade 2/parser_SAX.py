import time
import xml.sax as sax
import csv
import pandas as pd


    
class Listener(sax.ContentHandler):
    def __init__(self):
        self.id=""
        self.Latitude=""
        self.Longitude=""
        self.Tipo=""
        self.Nome=""
        self.dados = []
    def startElement(self, name, attrs):
        if name == "node":
            self.id = attrs.getValue('id')
            self.Latitude = attrs.getValue('lat')
            self.Longitude = attrs.getValue('lon')
        if name == 'tag':
            # if attrs.getValue('k') not in ['amenity', 'name']:
            #     return
            if attrs.getValue('k') == 'name':
                self.Nome = attrs.getValue('v')
            elif attrs.getValue('k') == 'amenity':
                self.Tipo = attrs.getValue('v')
     
    def endElement(self, name):
        if name == "node":
            if self.Nome and self.Tipo:
                self.dados.append({
                    'id': self.id,
                    'Latitude': self.Latitude,
                    'Longitude': self.Longitude,
                    'Tipo': self.Tipo,
                    'Nome': self.Nome
                })
            self.id = ""
            self.Latitude = ""
            self.Longitude = ""
            self.Nome = ""
            self.Tipo = ""
    # def endDocument(self):
        
def main():
    parser = sax.make_parser()

    Handler = Listener()
    parser.setContentHandler(Handler)
    print("Starting SAX Parser...")
    inicio = time.time()
    parser.parse("map_veneza.osm")
    fim = time.time()
    
    print(f"Tempo total: {fim - inicio}")
    
    
    with open('./SAX_PARSER.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'Latitude', 'Longitude', "Tipo", 'Nome']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(Handler.dados)
if __name__ == "__main__":
    main()