import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.descrpadrao import DescrPadrao

class DescrPadraoDao:

    _nome_tabela = 'descrpadrao'

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
        self.descrpadrao = DescrPadrao()

    def delete_all(self):
        cursor = self._banco.cursor()

        try:
            str_sql = f'DELETE FROM {self._nome_tabela}'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todas as Descricões Padrão: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"INSERT INTO {self._nome_tabela} "
            str_sql += "(Descricao_id,Descricao)"
            str_sql += " VALUES "
            str_sql += f"('{obj.get_descricao_id()}','{obj.get_descricao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir a Descrição Padrão: ', erro)
        finally:
            self._banco.commit()

    def update(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = f"UPDATE {self._nome_tabela} "
            str_sql += f"SET Descricao = '{obj.get_descricao()}' "
            str_sql += f"WHERE Descricao_id = '{obj.get_descricao_id()}'"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao atualizar a Descrição Padrão: ', erro)
        finally:
            self._banco.commit()

    def delete_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"DELETE FROM {self._nome_tabela} WHERE descricao_id = '{id}'"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir a Descrição Padrão: ', erro)
        finally:
            self._banco.commit()

    def find_by_id(self, id):

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT Descricao_Id,Descricao FROM {self._nome_tabela}" \
                      f" WHERE Descricao_id = '{id}'"

            cursor.execute(str_sql)

            lista = cursor.fetchall()

            if len(lista) > 0:
                return self.instantiate_descrpadrao(lista[0])

            return None

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar a Descrição Padrão: ', erro)

    def find_all(self):

        lista = []

        cursor = self._banco.cursor()

        try:
            str_sql = f"SELECT * FROM {self._nome_tabela} ORDER BY Descricao_Id"

            cursor.execute(str_sql)

            lista_descrpadrao = cursor.fetchall()

            for row in lista_descrpadrao:
                lista.append(self.instantiate_descrpadrao(row)) # Lista com os objetos de Descr Padrão

            return lista

        except sqlite3.Error as erro:
            raise ValueError('Erro ao encontrar todos as Descrições Padrão: ', erro)

    def instantiate_descrpadrao(self, lista):
        self.descrpadrao_temp = DescrPadrao()
        self.descrpadrao_temp.set_descricao_id(lista[0])
        self.descrpadrao_temp.set_descricao(lista[1])
        return self.descrpadrao_temp

    def carrega_descrpadrao_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.delete_all()

                for row in registro:
                    self.descrpadrao.set_descricao_id(row[0])
                    self.descrpadrao.set_descricao(row[1])

                    self.insert(self.descrpadrao)

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação das Descricões Padrão: {path}, Linha: {registro.line_num} : {e}')
        # finally:
        #     self._banco.commit()

    def carrega_descrpadrao_excel(self, path, nome_aba=''):
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
                self.descrpadrao.set_descricao_id(codigo)
                self.descrpadrao.set_descricao(lista_descricoes[i])
                self.insert(self.descrpadrao)
                i += 1

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        # finally:
        #     self._banco.commit()