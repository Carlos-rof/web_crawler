from datetime import date
from importlib import import_module
import requests
from bs4 import BeautifulSoup


class DOceanHtmlScrapy:
    req = requests.get("https://www.digitalocean.com/pricing/").text  # requisição get ao enpoint, com retorno em text
    soup = BeautifulSoup(req, 'html.parser')  # formatação do texto para html
    text_lines = soup.select('ul.priceBox')  # seleciona tag

    dict_terminal = {}

    @classmethod
    def save_scrapy(cls):
        for count in range(6):
            top_box = cls.text_lines[0].select('div.topBox')[count].get_text().split(' ')
            bottom_box_one = cls.text_lines[0].select('a > div:nth-child(2) > ul > li:nth-child(1)'
                                                      '')[count].get_text().split('/')
            bottom_box_two = cls.text_lines[0].select('a > div:nth-child(2) > ul > li:nth-child(2)')[count].get_text()
            bottom_box_thr = cls.text_lines[0].select('a > div:nth-child(2) > ul > li:nth-child(3)')[count].get_text()

            data = {
                'score': 'N/A',
                'storage': bottom_box_two,
                'cpu': bottom_box_one[1],
                'memory': bottom_box_one[0],
                'bandwidth': bottom_box_thr,
                'price': top_box[0],
                'hr_price': top_box[1],
                'date': str(date.today()),
                'tipo': 'regular',
                'scraped_page': 'https://www.digitalocean.com/pricing/'
            }
            local_db = import_module(f'models.LocalDB')
            local_db.DB.fill_db(**data)
            cls.dict_terminal.update({count: data})
        return cls.dict_terminal
