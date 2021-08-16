from importlib import import_module
from requests_html import HTMLSession
import demjson
import re
from datetime import date


class DOceanJSScrapy:
    session = HTMLSession()
    a = session.get(r"https://www.digitalocean.com/c91f2d98-7829554511fa4c770105.js")  # requisição get ao enpoint, com retorno em text

    text = a.text.split('k=')[1]  # seleciona a parte aonde estão os dados que o javascript ira atualizar na pagina

    tratamento1 = [item for item in text.split('{') if item]  # separa o texto no começo de cada chave, o que facilita o filtro
    tratamento2 = [item.split('}') for item in tratamento1 if item]  # separa o texto no fim de cada chave
    tratamento_id1 = [item[0].split(')') for item in tratamento2 if 'priceMo' in item[0]]  # filtra as partes do texto que contém o preço mensal do serviço
    tratamento_id2 = [item[0] for item in tratamento_id1 if 'priceMo' in item[0]]  # filtra os itens da lista que contém o preço mensal do serviço
    list_ids = list({''.join(re.findall('[0-9]', item)) for item in tratamento_id2})  # separa os IDs dos itens que serão atualizados

    data = {}
    dict_terminal_amd = {}
    dict_terminal_intel = {}

    @classmethod
    def save_scrapy(cls):
        for count in range(3):
            tratamento_type1 = cls.text.split(']')[count]
            tratamento_type2 = ''.join(re.findall('[a-zA-Z]', tratamento_type1.split(':')[0]))
            list_type_ids = [item for item in cls.list_ids if item in tratamento_type1]
            local_dict = {item: {'type': tratamento_type2} for item in list_type_ids}
            cls.data.update(local_dict)

        for count in range(1, len(cls.list_ids)+1):
            dict_id = [item for item in cls.list_ids if item in cls.tratamento1[count]]
            tratamento_dados1 = cls.tratamento1[count].split('cpuAmount:"')[1]
            tratamento_dados2 = '{' + f'cpuAmount:"{tratamento_dados1.split("}")[0]}' + '}'
            cls.data[dict_id[0]].update(demjson.decode(tratamento_dados2))

        for size_id in range(len(cls.list_ids)):
            tratamento_value1 = [item for item in cls.text.split('{droplet:') if f'size_id:"{cls.list_ids[size_id]}"' in item]
            usd_rate_per_month = tratamento_value1[0].split('usd_rate_per_month:"')[1].split('"')[0]
            usd_rate_per_hour = tratamento_value1[0].split('usd_rate_per_hour:"')[1].split('"')[0]
            cls.data[cls.list_ids[size_id]].update({'usd_rate_per_month': usd_rate_per_month, 'usd_rate_per_hour': usd_rate_per_hour})

        for key, item in cls.data.items():
            if 'premium' in item['type']:
                data_db = {
                    'score': 'N/A',
                    'storage': f'{item["ssdAmount"]} {item["ssdType"]}',
                    'cpu': item['cpuType'],
                    'memory': item['cpuAmount'],
                    'bandwidth': f'{item["transferAmount"]} transfer',
                    'price': f'${item["usd_rate_per_month"]}/mo',
                    'hr_price': f'${item["usd_rate_per_hour"]}/hour',
                    'date': str(date.today()),
                    'tipo': item['type'],
                    'scraped_page': 'https://www.digitalocean.com/pricing/'
                        }
                local_db = import_module(f'models.LocalDB')
                local_db.DB.fill_db(**data_db)
                if 'amd' in item['type'].lower():
                    cls.dict_terminal_amd.update({key: data_db})
                if 'intel' in item['type'].lower():
                    cls.dict_terminal_intel.update({key: data_db})
        return {'intel': cls.dict_terminal_intel, 'amd': cls.dict_terminal_amd}
