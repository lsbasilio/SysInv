from model.dao.daofactory import DaoFactory
from model.entities.enum.bens_status import BensStatus

class BensService:

    def __init__(self):
        daofactory = DaoFactory()
        self._dao = daofactory.create_bens_dao()

    def save_or_update(self, obj):
        # Faz tratamento pelo Status do Bem antes de Inventariar
        if obj.get_status_numerico() == BensStatus.Nao_Encontrado:
            obj.set_status(BensStatus.Novo)
            self._dao.insert(obj)
        else:
            if obj.get_status_numerico() == BensStatus.Pendente:
                    obj.set_status(BensStatus.Inventariado)
            self._dao.update(obj)

    def find_by_id(self, id):
        return self._dao.find_by_id(id)

    def find_all(self):
        return self._dao.find_all()

    def remove(self, obj):
        self._dao.delete_by_id(obj.get_numero_bem())