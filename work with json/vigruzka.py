import json


with open('mynew.json','r') as f:
    data=json.load(f)

print(data)