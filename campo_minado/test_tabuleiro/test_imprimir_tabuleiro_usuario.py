import unittest
from jogo.tabuleiro_usuario import Tabuleiro_usuario

class TestTabuleiroUsuario(unittest.TestCase):

    def test_imprimir_tabuleiro_8x8(self):
        tabuleiro = Tabuleiro_usuario(8, 8,10 )
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

    def test_imprimir_tabuleiro_10x16(self):
        tabuleiro = Tabuleiro_usuario(10, 16, 30)
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

    def test_imprimir_tabuleiro_24x24(self):
        tabuleiro = Tabuleiro_usuario(24, 24, 100)
        with self.subTest(tabuleiro=tabuleiro):
            self.assertEqual(tabuleiro.imprimir_tabuleiro(), None)

if __name__ == '__main__':
    unittest.main()
