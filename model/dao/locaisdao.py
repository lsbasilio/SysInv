import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.locais import Locais

class LocaisDao:

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
        self.locais = Locais()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = 'DELETE FROM locais'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Locais: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = "INSERT INTO locais "
            str_sql += "(Local_id,Descricao)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_local_id()},'{obj.get_descricao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir o Local: ', erro)

    def carrega_local_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.delete_all()

                for row in registro:
                    self.locais.set_local_id(int(row[0]))
                    self.locais.set_descricao(row[1])
                    self.insert(self.locais)

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação dos Locais: {path}, Linha: {registro.line_num} : {e}')
        finally:
            self._banco.commit()

    def carrega_local_excel(self, path, nome_aba=''):
        try:

            if nome_aba == '':
                planilha = pd.read_excel(path)
            else:
                planilha = pd.read_excel(path, sheet_name = nome_aba)

            self.delete_all()

            colunas = planilha.columns.tolist()

            lista_codigos = planilha[colunas[0]].tolist()
            lista_descricoes = planilha[colunas[1]].tolist()

            i = 0
            for codigo in lista_codigos:
                self.locais.set_local_id(codigo)
                self.locais.set_descricao(lista_descricoes[i])
                self.insert(self.locais)
                i += 1

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        finally:
            self._banco.commit()