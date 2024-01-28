from abc import ABC, abstractmethod


class AutenticacaoToken(ABC):
    @abstractmethod
    def validar(self, token:str):
        pass

    @abstractmethod
    def criar(self,id:str):
        pass