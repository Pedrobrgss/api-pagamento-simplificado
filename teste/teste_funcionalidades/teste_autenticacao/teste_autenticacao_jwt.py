import datetime
import unittest

import jwt

from src.config.gerenciameto_config import GerenciamentoConfig
from src.funcionalidades.autenticacao.autenticacao_jwt import AutenticacaoJwt


class TesteAutenticacaoJwt(unittest.TestCase):
    def setUp(self):
            gerenciameto_config = GerenciamentoConfig()
            self.autenticacao_jwt = AutenticacaoJwt(gerenciameto_config)

    def teste_criar(self):
        carga = {'id':1}
        resultado = self.autenticacao_jwt.criar(carga)
        self.assertEqual(resultado,"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.JrCtQPtzkN_h7C_q22vd-mIkuq--6ZJUVW0YvKhiqcI")

    def teste_validar_sucesso(self):
        carga = {"id":1, "exp":(datetime.datetime.now(tz=datetime.timezone.utc)+datetime.timedelta(seconds=30)).timestamp()}
        token = self.autenticacao_jwt.criar(carga)
        resultado=self.autenticacao_jwt.validar(token)
        self.assertEqual(resultado,carga)
    
    def teste_validar_fracasso(self):
        carga = {"id":1, "exp":(datetime.datetime.now(tz=datetime.timezone.utc)-datetime.timedelta(seconds=30)).timestamp()}
        token = self.autenticacao_jwt.criar(carga)
        with self.assertRaises(jwt.exceptions.ExpiredSignatureError):
            self.autenticacao_jwt.validar(token)

    