import sqlite3


class Db:

    def __init__(self):
        self._conn = None

    def get_connection(self):
        if self._conn == None:
            # self._caminho_banco = self._load_propertie('dblocation')
            # print(self._caminho_banco)
            # self._conn = sqlite3.connect(self._caminho_banco)
            self._conn = sqlite3.connect(self._load_propertie('dblocation'))

        return self._conn

    @staticmethod
    def _load_propertie(propriedade):
        arquivodb = open('C:\dev\SysInv\dbproperties.txt', 'r')
        for line in arquivodb.readlines():
            texto = line.split('=')
            if propriedade == texto[0]:
                texto[1] = texto[1].replace('\n','')
                # print('Dentro: ', texto[1])
                return texto[1]


