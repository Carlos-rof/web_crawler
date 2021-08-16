from models.LocalDB import DB
import json


class SaveJSON:
    result = DB.consult_db()  # retorna com todos os dados do banco local
    dict_save = {}

    for item in result:
        dict_model = {
            'tipo': f'{item.tipo} {item.score}',
            'storage': item.storage,
            'cpu': item.cpu,
            'memory': item.memory,
            'bandwidth': item.bandwidth,
            'price': item.price,
            'scraped page': item.scraped_page,
        }
        dict_save.update({item.id: dict_model})

    @classmethod
    def save(cls):
        with open('ScrapedData.json', 'w') as save_json:
            json.dump(cls.dict_save, save_json)
