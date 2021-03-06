from model.dao.daofactory import DaoFactory


class CentroDeCustoService:

    def __init__(self):
        daofactory = DaoFactory()
        self._dao = daofactory.create_centrodecusto_dao()

    def save_or_update(self, obj):
        if self._dao.find_by_id(obj.get_ccusto_id()) is None:
        # if obj.get_ccusto_id == 0:
           self._dao.insert(obj)
        else:
           self._dao.update(obj)

    def find_by_id(self, id):
        return self._dao.find_by_id(id)

    def find_ccusto_ativo(self):
        return self._dao.find_ccusto_ativo()

    def find_all(self):
        return self._dao.find_all()

    def altera_status_ccusto_ativo(self):
        return self._dao.altera_status_ccusto_ativo()

    def remove(self, obj):
        self._dao.delete_by_id(obj.get_ccusto_id())
