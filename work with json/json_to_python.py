import json
from random import randint
from datetime import datetime

str_json="""
{
"response":{
    "count": 5961878,
    "items":[{
        "first_name": "Елизавета",
        "id": 620471795,
        "last_name": "Сопова",
        "can_access_closed": true
    },{
        "first_name": "Роман",
        "id": 614752315,
        "last_name": "Малышев",
        "can_access_closed": true
    }]
}
}"""

print(type(str_json))

#преобразовуем в словарь
data = json.loads(str_json)

#проходимся по элементам слоаваря
# for item in data ['response']['items']:
#     print(item['first_name'],item['last_name'])


for item in data['response']['items']:
    del item["id"] #удалили ИД
    item['likes']=randint(100,200) #добавили лайки рандомно в диапазаон 100-200
    item['time'] =datetime.now().strftime('%d/%m/%y') # добавили время  
#print(data['response']['items'])


#создаем новый json\ indent нужен для отступов
#new_json=json.dumps(data,indent=2)
#print(new_json)

with open ('mynew.json','w') as file:
    json.dump(data,file,indent=3)

