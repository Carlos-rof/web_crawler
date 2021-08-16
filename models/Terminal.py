from prettytable import PrettyTable
from models.LocalDB import DB


class Terminal:
    result = DB.consult_db()  # retorna com todos os dados do banco local

    @classmethod
    def terminal(cls, dict_terminal):

        terminal_table = PrettyTable(['TIPO', 'CPU', 'MEMORY', 'STORAGE', 'BANDWIDTH', 'PRICE', 'SCORE'])  # cabeçalho
        # alinha coluna ao centro
        terminal_table.align['TIPO'] = 'c'
        terminal_table.align['CPU'] = 'c'
        terminal_table.align['MEMORY'] = 'c'
        terminal_table.align['STORAGE'] = 'c'
        terminal_table.align['BANDWIDTH'] = 'c'
        terminal_table.align['PRICE'] = 'c'
        terminal_table.align['SCORE'] = 'c'

        terminal_table.padding_width = 3  # espaçamento
        for key, value in dict_terminal.items():
            terminal_table.add_row(
                [value["tipo"], value["cpu"], value["memory"], value["storage"], value["bandwidth"], value["price"],
                 value["score"]])

        return terminal_table

    @classmethod
    def print_terminal(cls, page, table, dict_terminal):
        print(f'==> Scrapy of page: {page}     -     Table: {table}:')
        terminal = cls.terminal(dict_terminal)
        print(terminal, '\n')
        terminal.clear()  # limpa o terminal_table após exibição
