from db.db import Db
from model.dao.impl.locaisdaoSqLite import LocaisDaoSqLite


class DaoFactory:

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()

    def create_locais_dao(self):
        locaisdaosqlite = LocaisDaoSqLite(self._banco)
        return locaisdaosqlite