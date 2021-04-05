import sqlite3
from db.db import Db
import csv
import pandas as pd
from model.entities.descrcomplementar import DescrComplementar

class DescrComplementarDao:
    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()
        self.descrcomplementar = DescrComplementar()

    def delete_all(self):

        cursor = self._banco.cursor()

        try:
            str_sql = 'DELETE FROM descrcomplementar'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todas as Descricões Complementares: ', erro)
        finally:
            self._banco.commit()

    def insert(self, obj):

        cursor = self._banco.cursor()

        try:
            str_sql = "INSERT INTO descrcomplementar "
            str_sql += "(Descricao_id,Descricao)"
            str_sql += " VALUES "
            str_sql += f"('{obj.get_descricao_id()}','{obj.get_descricao()}')"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir a descrição padrão: ', erro)

    def carrega_descrcomplementar_csv(self, path):
        try:

            with open(path) as csvfile:
                registro = csv.reader(csvfile, delimiter=';')

                self.delete_all()

                for row in registro:
                    self.descrcomplementar.set_descricao_id(row[0])
                    self.descrcomplementar.set_descricao(row[1])

                    self.insert(self.descrcomplementar)

                csvfile.close()

        except FileNotFoundError:
            raise ValueError(f'O arquivo CSV informado: {path} não existe!')
        except csv.Error as e:
            print(f'Erro na Importação das Descricões Complementares: {path}, Linha: {registro.line_num} : {e}')
        finally:
            self._banco.commit()

    def carrega_descrcomplementar_excel(self, path, nome_aba=''):
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
                self.descrcomplementar.set_descricao_id(codigo)
                self.descrcomplementar.set_descricao(lista_descricoes[i])
                self.insert(self.descrcomplementar)
                i += 1

        except FileNotFoundError:
            raise ValueError(f'O arquivo Excel informado: {path} não existe!')
        finally:
            self._banco.commit()


