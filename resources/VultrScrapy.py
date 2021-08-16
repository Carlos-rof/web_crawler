from datetime import date
from importlib import import_module
import requests
from bs4 import BeautifulSoup


class VultrScrapy:
    req = requests.get("https://www.vultr.com/products/cloud-compute/").text  # requisição get ao enpoint, com retorno em text
    soup = BeautifulSoup(req, 'html.parser')  # formatação do texto para html
    text_lines = soup.select('div.pt__row-content')  # seleciona tag

    dict_terminal = {}

    @classmethod
    def save_scrapy(cls):
        for div in range(len(cls.text_lines)):
            text_lines = cls.soup.select('div.pt__row-content')[div].get_text().replace('\t', '').splitlines()
            text_list = []
            for line in text_lines:
                if line and line != 'IPv6':  # cria lista sem o item 'IPv6'
                    text_list.append(line)
            data = {
                'score': text_list[1],
                'storage': text_list[2],
                'cpu': text_list[3],
                'memory': text_list[4],
                'bandwidth': text_list[5],
                'price': text_list[6],
                'hr_price': text_list[7],
                'date': str(date.today()),
                'tipo': 'vultr',
                'scraped_page': 'https://www.vultr.com/products/cloud-compute/#pricing'
            }

            local_db = import_module(f'models.LocalDB')
            local_db.DB.fill_db(**data)
            cls.dict_terminal.update({div: data})
        return cls.dict_terminal
