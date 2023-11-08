import random

class Tabuleiro_usuario:
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        tabuleiro = [['?' for _ in range(self.colunas)] for _ in range(self.linhas)]

        return tabuleiro
    
    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))