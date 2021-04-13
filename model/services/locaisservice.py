from model.dao.daofactory import DaoFactory


class LocaisService:

    def __init__(self):
        daofactory = DaoFactory()
        self._dao = daofactory.create_locais_dao()

    def save_or_update(self, obj):
        if self._dao.find_by_id(obj.get_local_id()) is None:
           self._dao.insert(obj)
        else:
           self._dao.update(obj)

    def find_all(self):
        return self._dao.find_all()

    def remove(self, obj):
        self._dao.delete_by_id(obj.get_local_id())