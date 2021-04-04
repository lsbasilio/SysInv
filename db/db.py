import sqlite3


class Db:

    def __init__(self):
        self._conn = None

    def get_connection(self):
        if self._conn == None:
            self._conn = sqlite3.connect(self._load_properties('dblocation'))

        return self._conn

    @staticmethod
    def _load_properties(propriedade):
        try:
            arquivodb = open('..\dbproperties.txt', 'r')
            for line in arquivodb:
                texto = line.split('=')
                if propriedade == texto[0]:
                    texto[1] = texto[1].rstrip('\n') #texto[1].replace('\n','')
                    return texto[1]
            arquivodb.close()
        except FileNotFoundError:
            raise ValueError('Arquivo de configuração do banco não encontrado')
        except IOError:
            raise ValueError('Erro ao abrir o arquivo de configuração do banco')

