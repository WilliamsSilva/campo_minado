import unittest
from jogo.tabuleiro_minado import Tabuleiro_minado

class TestTabuleiroMinado(unittest.TestCase):

#Sem bombas
    #linha 0
    def test_contar_bombas_ao_redor_0x0__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 0x0 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 0), 0)

    def test_contar_bombas_ao_redor_0x1__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 0x1 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 1), 0)

    def test_contar_bombas_ao_redor_0x4__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 0x4 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 4), 0)

    def test_contar_bombas_ao_redor_0x7__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 0x7 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 7), 0)
    
    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 1x0 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 0)

    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 1x1 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 0)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 1x4 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 0)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 1x7 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 0)
    
    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 4x0 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 0)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 4x1 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 0)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 4x4 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 0)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 4x7 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 0)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x0__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 7x0 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 0), 0)

    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 7x1 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 0)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 7x4 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 0)

    def test_contar_bombas_ao_redor_7x7__tabuleiro_8x8(self):
        # Tabuleiro sem bombas, a célula 7x7 não deve ter bombas ao redor
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 7), 0)

#Com uma bomba
    #linha 0
    def test_contar_bombas_ao_redor_0x0__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 0x0 com 1 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 0), 1)

    def test_contar_bombas_ao_redor_0x1__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 0x1 com 1 bombas
        tabuleiro = [['-', '-', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 1), 1)

    def test_contar_bombas_ao_redor_0x4__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 0x4 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 4), 1)

    def test_contar_bombas_ao_redor_0x7__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 0x7 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 7), 1)
    
    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 1x0 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 1)

    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 1)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com  1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 1)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 1x7 com bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 1)
    
    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 4x0 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 1)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 1)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 1)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 4x7 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 1)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x0__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 7x0 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 0), 1)

    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 7x1 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 1)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 7x4 com 1 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 1)

    def test_contar_bombas_ao_redor_7x7__tabuleiro_8x8_1_bomba(self):
        # Tabuleiro sem bombas, a célula 7x7 com bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 7), 1)



#com duas
    #linha 0
    def test_contar_bombas_ao_redor_0x0__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 0x0 com 2 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 0), 2)

    def test_contar_bombas_ao_redor_0x1__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 0x1 com 2 bombas
        tabuleiro = [['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 1), 2)

    def test_contar_bombas_ao_redor_0x4__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 0x4 com 2 bombas
        tabuleiro = [['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 4), 2)

    def test_contar_bombas_ao_redor_0x7__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 0x7 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 7), 2)
    
    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 1x0 com 2 bombas
        tabuleiro = [['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 2)
    
    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 2x1 com 2 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 2)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 2)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 1x7 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 2)

    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 4x0 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 2)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 2)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 2)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 4x7 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 2)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x0__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 7x0 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 0), 2)

    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 7x1 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 2)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 7x4 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 2)

    def test_contar_bombas_ao_redor_7x7__tabuleiro_8x8_2_bomba(self):
        # Tabuleiro sem bombas, a célula 7x7 com 2 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 7), 2)

#com tres
    #linha 0
    def test_contar_bombas_ao_redor_0x0__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 0x0 com 3 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 0), 3)

    def test_contar_bombas_ao_redor_0x1__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 0x1 com 3 bombas
        tabuleiro = [['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 1), 3)

    def test_contar_bombas_ao_redor_0x4__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 0x4 com 3 bombas
        tabuleiro = [['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 4), 3)

    def test_contar_bombas_ao_redor_0x7__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 0x7 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 7), 3)
    
    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 1x0 com 3 bombas
        tabuleiro = [['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 3)

    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 3 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 3)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 3 bombas
        tabuleiro = [['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 3)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 1x7 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 3)
    
    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 4x0 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 3)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 3)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 3)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 4x7 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 3)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x0__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 7x0 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 0), 3)

    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 7x1 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 3)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 7x4 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 3)

    def test_contar_bombas_ao_redor_7x7__tabuleiro_8x8_3_bomba(self):
        # Tabuleiro sem bombas, a célula 7x7 com 3 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 7), 3)

    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 1x0 com 4 bombas
        tabuleiro = [['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 4)

    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 4 bombas
        tabuleiro = [['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 4)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 4 bombas
        tabuleiro = [['-', '-', '-','ó', 'ó', '-','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 4)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 1x7 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 4)
    
    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 4x0 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 4)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 4)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 4)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 4x7 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','-', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 4)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 7x1 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 4)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8_4_bomba(self):
        # Tabuleiro sem bombas, a célula 7x4 com 4 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','ó', 'ó', '-','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 4)
    def test_contar_bombas_ao_redor_0x1__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 0x1 com 5 bombas
        tabuleiro = [['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 1), 5)

    def test_contar_bombas_ao_redor_0x4__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 0x4 com 5 bombas
        tabuleiro = [['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 0, 4), 5)

    
    #linha 1
    def test_contar_bombas_ao_redor_1x0__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 1x0 com 5 bombas
        tabuleiro = [['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 0), 5)

    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 5 bombas
        tabuleiro = [['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 5)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 5 bombas
        tabuleiro = [['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 5)

    def test_contar_bombas_ao_redor_1x7__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 1x7 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 7), 5)
    
    #linha 4
    def test_contar_bombas_ao_redor_4x0__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 4x0 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 0), 5)

    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 5)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','-', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 5)

    def test_contar_bombas_ao_redor_4x7__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 4x7 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','ó', '-'],
                     ['-', '-', '-','-', '-', '-','ó', 'ó'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 7), 5)
    
    #linha 7
    def test_contar_bombas_ao_redor_7x1__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 7x1 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 1), 5)

    def test_contar_bombas_ao_redor_7x4__tabuleiro_8x8_5_bomba(self):
        # Tabuleiro sem bombas, a célula 7x4 com 5 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 7, 4), 5)

    #linha 1
    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_6_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 6 bombas
        tabuleiro = [['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 6)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_6_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 6 bombas
        tabuleiro = [['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 6)

    
    #linha 4
    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_6_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 6 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 6)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_6_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 6 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 6)
        
# 7 bombas
    #linha 1
    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_7_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 7 bombas
        tabuleiro = [['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 7)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_7_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 7 bombas
        tabuleiro = [['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 7)

    
    #linha 4
    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_7_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 7 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', '-','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 7)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_7_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 7 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 7)
#8 bombas
    #linha 1
    def test_contar_bombas_ao_redor_1x1__tabuleiro_8x8_8_bomba(self):
        # Tabuleiro sem bombas, a célula 1x1 com 8 bombas
        tabuleiro = [['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 1), 8)

    def test_contar_bombas_ao_redor_1x4__tabuleiro_8x8_8_bomba(self):
        # Tabuleiro sem bombas, a célula 1x4 com 8 bombas
        tabuleiro = [['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 1, 4), 8)

    
    #linha 4
    def test_contar_bombas_ao_redor_4x1__tabuleiro_8x8_8_bomba(self):
        # Tabuleiro sem bombas, a célula 4x1 com 8 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['ó', '-', 'ó','-', '-', '-','-', '-'],
                     ['ó', 'ó', 'ó','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 1), 8)

    def test_contar_bombas_ao_redor_4x4__tabuleiro_8x8_8_bomba(self):
        # Tabuleiro sem bombas, a célula 4x4 com 8 bombas
        tabuleiro = [['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','ó', '-', 'ó','-', '-'],
                     ['-', '-', '-','ó', 'ó', 'ó','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],
                     ['-', '-', '-','-', '-', '-','-', '-'],]
        tabuleiro_minado = Tabuleiro_minado(8, 8, 0)
        self.assertEqual(tabuleiro_minado.contar_bombas_ao_redor(tabuleiro, 4, 4), 8)


    
if __name__ == '__main__':
    unittest.main()





