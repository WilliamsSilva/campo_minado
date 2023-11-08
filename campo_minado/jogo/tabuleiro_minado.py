import random

class Tabuleiro_minado:
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        tabuleiro = [['0' for _ in range(self.colunas)] for _ in range(self.linhas)]

        for _ in range(self.bombas):
            linha, coluna = random.randint(0, self.linhas - 1), random.randint(0, self.colunas - 1)
            while tabuleiro[linha][coluna] == 'ó':
                linha, coluna = random.randint(0, self.linhas - 1), random.randint(0, self.colunas - 1)
            tabuleiro[linha][coluna] = 'ó'

        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if tabuleiro[linha][coluna] != 'ó':
                    count = self.contar_bombas_ao_redor(tabuleiro, linha, coluna)
                    tabuleiro[linha][coluna] = str(count)

        return tabuleiro
    
    def contar_bombas_ao_redor(self, tabuleiro, linha, coluna):
        direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        count = 0
        for dx, dy in direcoes:
            x, y = linha + dx, coluna + dy
            if 0 <= x < self.linhas and 0 <= y < self.colunas and tabuleiro[x][y] == 'ó':
                count += 1
        return count

    #imprime o tabuleiro de bombas
    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))