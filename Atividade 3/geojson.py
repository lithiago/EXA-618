import json
import pandas as pd



file_csv = pd.read_csv('Atividade 2/DOM_PARSER.csv')


geo_json = {}


geo_json["type"] = "FeatureCollection"
geo_json["features"] = []

object_from_csv = {}

for v, k in file_csv.iterrows():
    object_from_csv['type'] = "Feature"
    object_from_csv['geometry'] = {
        "type": "Point",
        "coordinates": [
            k['Longitude'],
            k['Latitude']
        ]
    }
    object_from_csv['properties'] ={
        "nome": k['Nome'],
        "tipo": k['Tipo']
    }
    geo_json["features"].append(object_from_csv)
    
    object_from_csv = {}


output = json.dumps(geo_json, indent=4, ensure_ascii=False)

print(output)


with open("geo.json", "w") as f:
    f.write(output)
