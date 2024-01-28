import psycopg2.pool
from config.gerenciameto_config import GerenciamentoConfig
from funcionalidades.banco_de_dados.banco_de_dados import BancoDeDados


class BancoDeDadosPostgress(BancoDeDados):
    def __init__(self, gerenciamento_config: GerenciamentoConfig):
        self._pool = psycopg2.pool.SimpleConnectionPool(
            user=gerenciamento_config.get('USER_POSTGRESS'),
            host=gerenciamento_config.get('HOST_POSTGRESS'),
            port=gerenciamento_config.get('PORTA'),
            password=gerenciamento_config.get('PASSWORD_POSTGRESS'),
            minconn=gerenciamento_config.get('MIN_CONEXAO'),
            maxconn=gerenciamento_config.get('MAX_CONEXAO'),
            dbname=gerenciamento_config.get('DATABASE_POSTGRESS')
        )
    
    def _executar(self,query:str,conexao):
        cursor = conexao.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def query_transacao(self,query:str):
        conexao = self._pool.getconn()
        resultado = []
        try:
            resultado = self._executar(query,conexao)
            conexao.commit()
            
        except Exception as e:
            conexao.rollback()
            raise

        finally:
            self._pool.putconn(conexao)

        return resultado

    def query(self,query:str):
        conexao = self._pool.getconn()
        resultado = self._executar(query,conexao)
        self._pool.putconn(conexao)
        return resultado

    def fechar(self):
        self._pool.closeall()
    