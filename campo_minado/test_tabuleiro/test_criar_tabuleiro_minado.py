import unittest
from jogo.tabuleiro_minado import Tabuleiro_minado

class TestTabuleiroMinado(unittest.TestCase):
    def test_criar_tabuleiro_minado_facil(self):
        # Teste para criar um tabuleiro fácil
        linhas, colunas, bombas = 8, 8, 10
        tabuleiro_minado = Tabuleiro_minado(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o número de bombas no tabuleiro é igual ao número de bombas especificado
        bomba_count = sum(linha.count('ó') for linha in tabuleiro)
        self.assertEqual(bomba_count, bombas)

    def test_criar_tabuleiro_minado_intermediario(self):
        # Teste para criar um tabuleiro intermediário
        linhas, colunas, bombas = 10, 16, 30
        tabuleiro_minado = Tabuleiro_minado(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o número de bombas no tabuleiro é igual ao número de bombas especificado
        bomba_count = sum(linha.count('ó') for linha in tabuleiro)
        self.assertEqual(bomba_count, bombas)

    def test_criar_tabuleiro_minado_dificil(self):
        # Teste para criar um tabuleiro difícil
        linhas, colunas, bombas = 24, 24, 100
        tabuleiro_minado = Tabuleiro_minado(linhas, colunas, bombas)
        tabuleiro = tabuleiro_minado.criar_tabuleiro()
        
        # Verifica se o tabuleiro foi criado corretamente
        self.assertEqual(len(tabuleiro), linhas)
        self.assertEqual(len(tabuleiro[0]), colunas)
        
        # Verifica se o número de bombas no tabuleiro é igual ao número de bombas especificado
        bomba_count = sum(linha.count('ó') for linha in tabuleiro)
        self.assertEqual(bomba_count, bombas)

if __name__ == '__main__':
    unittest.main()
