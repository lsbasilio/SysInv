import sqlite3


class Db:

    def __init__(self):
        self._conn = None

    def get_connection(self):
        try:
            if self._conn is None:
                self._conn = sqlite3.connect(self._load_properties('dblocation'))

            return self._conn

        except sqlite3.Error as erro:
            print('Erro ao conectar ao Banco: ', erro)

    def close_connection(self):
        try:
            if self._conn is not None:
                self._conn.close()

        except sqlite3.Error as erro:
            print('Erro ao fechar a conexão com o Banco: ', erro)

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

