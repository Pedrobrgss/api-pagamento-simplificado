import unittest
from src.config.gerenciameto_config import GerenciamentoConfig
class TesteGerenciamentoConfig(unittest.TestCase):
    def teste_carregamento(self):
        gerenciamento_config=GerenciamentoConfig()
        self.assertIsInstance(gerenciamento_config,GerenciamentoConfig)


if __name__=='__main__':
    unittest.main()