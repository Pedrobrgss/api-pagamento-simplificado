import os

from dotenv import load_dotenv

class GerenciamentoConfig:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GerenciamentoConfig, cls).__new__(cls)
            # Inicialize as variáveis de ambiente aqui
            cls._instancia._env_variables = {}
            cls._instancia._carregar_variaveis()
        return cls._instancia

    def get(self, key):
        """Obtém o valor da variável de ambiente com uma opção de valor padrão."""
        retorno = self._env_variables.get(key,'')
        if retorno=='' or retorno==None:
            raise ValueError('Variável de ambiente não configurada!')
        
        return retorno


    def _carregar_variaveis(self):
        """Define o valor de uma variável de ambiente."""
        load_dotenv()
        self._env_variables = {key: os.getenv(key) for key in os.environ}
        
        for value in self._env_variables:
            if value == None or value=="":
                raise ValueError('Erro ao carregar variáveis de ambiente')
