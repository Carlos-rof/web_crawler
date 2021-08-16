from models.LocalDB import DB
import pandas


class SaveCSV:
    result = DB.consult_db()  # retorna com todos os dados do banco local
    format_csv = {
            'ID': [item.id for item in result],
            'TIPO': [item.tipo for item in result],
            'CPU': [item.cpu for item in result],
            'MEMORY': [item.memory for item in result],
            'STORAGE': [item.storage for item in result],
            'BANDWIDTH': [item.bandwidth for item in result],
            'PRICE': [item.price for item in result],
            'SCRAPED PAGE': [item.scraped_page for item in result],
            'SCORE': [item.score for item in result]

    }

    @classmethod
    def save(cls):
        save_csv = pandas.DataFrame(cls.format_csv)
        save_csv.to_csv('ScrapedData.csv', index=False, sep=';')
