from abc import ABC, abstractmethod


class BensDao(ABC):

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def insert(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def carrega_csv(self, path):
        pass

    @abstractmethod
    def carrega_excel(self, path, nome_aba=''):
        pass

    @abstractmethod
    def salvar_campos_originais(self):
        pass

    @abstractmethod
    def update_bens_pendentes(self):
        pass

