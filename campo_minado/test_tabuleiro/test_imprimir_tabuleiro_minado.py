import unittest
from jogo.tabuleiro_minado import Tabuleiro_minado

class TestTabuleiroMinado(unittest.TestCase):

    def test_imprimir_tabuleiro_minado_8x8(self):
        tabuleiro = Tabuleiro_minado(8, 8,10 )
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

    def test_imprimir_tabuleiro_minado_10x16(self):
        tabuleiro = Tabuleiro_minado(10, 16, 30)
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

    def test_imprimir_tabuleiro_minado_24x24(self):
        tabuleiro = Tabuleiro_minado(24, 24, 100)
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

if __name__ == '__main__':
    unittest.main()