import jwt
from src.config.gerenciameto_config import GerenciamentoConfig
from src.funcionalidades.autenticacao.autenticacao_token import AutenticacaoToken


class AutenticacaoJwt(AutenticacaoToken):
    def __init__(self, gerenciamento_config:GerenciamentoConfig):
        self._jwt = jwt
        self._config = gerenciamento_config
        self._algoritmo = 'HS256'

    def criar(self, carga:dict):
        return self._jwt.encode(carga, self._config.get('SEGREDO_JWT'),algorithm=self._algoritmo)
    
    def validar(self, token: str):
        return self._jwt.decode(token,self._config.get('SEGREDO_JWT'),algorithms=[self._algoritmo])
