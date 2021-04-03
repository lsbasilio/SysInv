import sqlite3
from db.db import Db


class CentroDeCustoDao:

    def __init__(self):
        self._db = Db()
        self.banco = self._db.get_connection()

    def delete_all(self):
        cursor = self.banco.cursor()

        try:
            str_sql = 'DELETE FROM centrodecusto'
            cursor.execute(str_sql)
        except sqlite3.Error as erro:
            raise ValueError('Erro ao excluir todos os Centros de Custo: ', erro)
        finally:
            self.banco.commit()

    def insert(self, obj):

        cursor = self.banco.cursor()

        try:
            str_sql = "INSERT INTO centrodecusto "
            str_sql += "(Ccusto_id,Descricao,Status,Data_Inicio,Data_Fim,Pendentes,Inventariados,Novos)"
            str_sql += " VALUES "
            str_sql += f"({obj.get_ccusto_id()},'{obj.get_descricao()}',{obj.get_status()},'{obj.get_data_inicio()}','{obj.get_data_fim()}',{obj.get_pendentes()},{obj.get_inventariados()},{obj.get_novos()})"

            cursor.execute(str_sql)

        except sqlite3.Error as erro:
            raise ValueError('Erro ao inserir o Centro de Custo: ', erro)
        # finally:
        #     banco.commit()
