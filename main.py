from importlib import import_module
from models.Terminal import Terminal
from resources.VultrScrapy import VultrScrapy
from resources.DOceanJSScrapy import DOceanJSScrapy
from resources.DOceanHtmlScrapy import DOceanHtmlScrapy

if __name__ == '__main__':

    dict_terminal = VultrScrapy.save_scrapy()  # Scrapy do site Vultr, com o retorno do endpoint em html
    Terminal.print_terminal('VULTR', 'GENERAL', dict_terminal)

    dict_terminal = DOceanHtmlScrapy.save_scrapy()  # Scrapy do site Digital Ocean, com o retorno do endpoint em html
    Terminal.print_terminal('DIGITAL OCEAN', 'REGULAR', dict_terminal)

    dict_terminal = DOceanJSScrapy.save_scrapy()  # Scrapy do site Digital Ocean, usando a application javascript da pagina, para as tabelas Premium Intel e AMD
    Terminal.print_terminal('DIGITAL OCEAN', 'PREMIUM INTEL', dict_terminal['intel'])
    Terminal.print_terminal('DIGITAL OCEAN', 'PREMIUM AMD', dict_terminal['amd'])

    CSV = import_module(f'models.SaveCSV')  # Import local da classe SaveCSV
    JSON = import_module(f'models.SaveJSON')  # Import local da classe SaveJSON

    CSV.SaveCSV.save()
    JSON.SaveJSON.save()
