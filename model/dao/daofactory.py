from db.db import Db
from model.dao.impl.locaisdaoSqLite import LocaisDaoSqLite
from model.dao.impl.descrpadraodaoSqLite import DescrPadraoDaoSqLite
from model.dao.impl.descrcomplementardaoSqLite import DescrComplementarDaoSqLite
from model.dao.impl.centrodecustodaoSqLite import CentroDeCustoDaoSqLite
from model.dao.impl.bensdaoSqLite import BensDaoSqLite


class DaoFactory:

    def __init__(self):
        self._db = Db()
        self._banco = self._db.get_connection()

    def create_locais_dao(self):
        locaisdaosqlite = LocaisDaoSqLite(self._banco)
        return locaisdaosqlite

    def create_descrpadrao_dao(self):
        descrpadraodaosqlite = DescrPadraoDaoSqLite(self._banco)
        return descrpadraodaosqlite
    
    def create_descrcomplementar_dao(self):
        descrcomplementardaosqlite = DescrComplementarDaoSqLite(self._banco)
        return descrcomplementardaosqlite

    def create_centrodecusto_dao(self):
        centrodecustodaoSqLite = CentroDeCustoDaoSqLite(self._banco)
        return centrodecustodaoSqLite

    def create_bens_dao(self):
        bensdaoSqLite = BensDaoSqLite(self._banco)
        return bensdaoSqLite
