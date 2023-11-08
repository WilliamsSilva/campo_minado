import unittest
from jogo.tabuleiro_usuario import Tabuleiro_usuario

class TestTabuleiroMinado(unittest.TestCase):
    def test_criar_tabuleiro_usuario_facil(self):
        # Teste para criar um tabuleiro fácil
        linhas, colunas, bombas = 8, 8, 10
        tabuleiro_minado = Tabuleiro_usuario(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o tabuleiro contém apenas '?'
        self.assertTrue(all(all(cell == '?' for cell in linha) for linha in tabuleiro))

    def test_criar_tabuleiro_usuario_intermediario(self):
        # Teste para criar um tabuleiro intermediário
        linhas, colunas, bombas = 10, 16, 30
        tabuleiro_minado = Tabuleiro_usuario(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o tabuleiro contém apenas '?'
        self.assertTrue(all(all(cell == '?' for cell in linha) for linha in tabuleiro))

    def test_criar_tabuleiro_usuario_dificil(self):
        # Teste para criar um tabuleiro difícil
        linhas, colunas, bombas = 24, 24, 100
        tabuleiro_minado = Tabuleiro_usuario(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o tabuleiro contém apenas '?'
        self.assertTrue(all(all(cell == '?' for cell in linha) for linha in tabuleiro))

if __name__ == '__main__':
    unittest.main()
