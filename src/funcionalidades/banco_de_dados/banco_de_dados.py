from abc import ABC, abstractmethod


class BancoDeDados(ABC):
    @abstractmethod
    def query_transacao(self, query: str):
        pass

    @abstractmethod
    def query(self, query: str):
        pass

    @abstractmethod
    def fechar():
        pass