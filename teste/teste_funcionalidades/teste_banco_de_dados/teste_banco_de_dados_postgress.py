import unittest
import psycopg2
from src.funcionalidades.banco_de_dados.banco_de_dados_postgress import BancoDeDadosPostgress
from src.config.gerenciameto_config import GerenciamentoConfig

class TesteBancoDeDadosPostgress(unittest.TestCase):
    def setUp(self):
        gerenciamento_config=GerenciamentoConfig()
        self.banco_de_dados_postgress=BancoDeDadosPostgress(gerenciamento_config)
    def teste_intancia(self):
        self.assertIsInstance(self.banco_de_dados_postgress,BancoDeDadosPostgress)

    def teste_de_fechar(self):
        self.banco_de_dados_postgress.fechar()

    def teste_query_transacao_sucesso(self):
        try:
            resultado = self.banco_de_dados_postgress.query_transacao("SELECT 1;")
            self.assertEqual(resultado,[(1,)])
        except psycopg2.Error as e:
            self.fail(f"Falha ao executar operação com transação no PostgreSQL:{e}")

    def teste_query_transacao_falha(self):
        sucesso = False
        try:
            resultado = self.banco_de_dados_postgress.query_transacao("SELECT * FROM TABELA_INCORRETA;")
            self.assertEqual(resultado,[(1,)])
        except psycopg2.Error as e:
            sucesso = True
            
        self.assertTrue(sucesso)
        
    def teste_query(self):
        try:
            resultado = self.banco_de_dados_postgress.query("SELECT 1;")
            self.assertEqual(resultado,[(1,)])
        except psycopg2.Error as e:
            self.fail(f"Falha ao executar operação no PostgreSQL:{e}")

        

if __name__=='__main__':
    unittest.main()