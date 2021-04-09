import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.locais import Locais
from model.dao.locaisdao import LocaisDao


class LocaisDaoSqLite(LocaisDao):

    _nome_tabela = 'locais'

    def __init__(self, conn):
        self._banco = conn
        self.locais = Locais()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = f'DELETE FROM {self._nome_tabela}'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Locais: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"INSERT INTO {self._nome_tabela} "
            str_sql += "(Local_id,Descricao)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_local_id()},'{obj.get_descricao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir o Local: ', erro)
        finally:
            self._banco.commit()

    def update(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Descricao = '{obj.get_descricao()}' "
            str_sql += f"WHERE Local_id = {obj.get_local_id()}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar o Local: ', erro)
        finally:
            self._banco.commit()

    def delete_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"DELETE FROM {self._nome_tabela} WHERE Local_id = {id}"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir o Local: ', erro)
        finally:
            self._banco.commit()

    def find_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT Local_Id,Descricao FROM {self._nome_tabela} " \
                      f"WHERE Local_id = {id}"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return self.instantiate_local(lista[0])

            return None

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar o Local: ', erro)

    def find_all(self):

        lista = []

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} ORDER BY Descricao"

            cursor.execute(str_sql)

            lista_locais = cursor.fetchall()

            for row in lista_locais:
                lista.append(self.instantiate_local(row)) # Lista com os objetos de Local

            return lista

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar todos os Locais: ', erro)

    def instantiate_local(self, lista):
        self.locais_temp = Locais()
        self.locais_temp.set_local_id(lista[0])
        self.locais_temp.set_descricao(lista[1])
        return self.locais_temp

    def carrega_csv(self, path):
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
        # finally:
        #     self._banco.commit()

    def carrega_excel(self, path, nome_aba=''):
        try:

            if nome_aba == '':
                planilha = pd.read_excel(path, na_filter=False)
            else:
                planilha = pd.read_excel(path, sheet_name=nome_aba, na_filter=False)

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
        # finally:
        #     self._banco.commit()