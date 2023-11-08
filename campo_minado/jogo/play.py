from typing import Self
from tabuleiro_minado import Tabuleiro_minado
from tabuleiro_usuario import Tabuleiro_usuario
import os
from datetime import datetime
import json

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Play:

    def main(self):
        linha = 0
        coluna = 0
        bombas = 0
        bandeiras = 0
        jogo_continua = True
        
        historico = []

        # Carregue o histórico anterior se existir
        try:
            with open('historico_partidas.json', 'r') as arquivo:
                historico = json.load(arquivo)
        except FileNotFoundError:
            historico = []

#MENU INICIAL ESCOLHA DO NIVEL
        while jogo_continua == True:
            partida_continua = True
            print("Bem-vindo ao Campo Minado!")
            print("Escolha uma opção:")
            print("1. Fácil")
            print("2. Intermediário")
            print("3. Difícil")
            print("4. Encerrar Jogo")
            print("5. Ver historico")
            nivel = input("Digite o número da opção des1ejada: ")

            if nivel == "1":
                linha = 8
                coluna = 8
                bombas = 10
                limpar_terminal()


                
            elif nivel == "2":
                linha = 10
                coluna = 16
                bombas = 30
                limpar_terminal()

            elif nivel == "3":
                linha = 24
                coluna = 24
                bombas = 100
                limpar_terminal()

            elif nivel == "4":
                print ("ENCERRANDO JOGO...")
                jogo_continua = False
                limpar_terminal()
            
            elif nivel == "5":
                verhistorico(historico)
                partida_continua = False
                limpar_terminal()


    #INSTANCIANDO TABULEIROS
            tabuleiro_minado = Tabuleiro_minado(linha,coluna, bombas)
            tabuleiro_usuario = Tabuleiro_usuario (linha, coluna, bombas)  

            
            hora_inicio = datetime.now()
            while partida_continua == True:
                tabuleiro_usuario.imprimir_tabuleiro()
                
                print("Escolha sua proxima ação:")
                print("1. Marcar uma célula")
                print("2. Abrir uma célula")
                print("3. Desmarcar uma célula")
                print("4. Encerrar partida")
                escolha = input("Digite o número da opção desejada: ")
                
                #marcar celula
                if escolha == "1":
                    print('Para marcar a celula digite:')
                    linha = int(input("A coordenada da linha: "))
                    coluna = int(input("A coordenada da coluna: "))
                    if 0 <= linha < tabuleiro_usuario.linhas and 0 <= coluna < tabuleiro_usuario.colunas:
                        if tabuleiro_usuario.tabuleiro[linha][coluna] == "?":
                            # Marca a célula no Tabuleiro_usuario
                            tabuleiro_usuario.tabuleiro[linha][coluna] = "M"
                            if tabuleiro_minado.tabuleiro[linha][coluna] == "ó":
                                bandeiras = bandeiras + 1
                                if bandeiras == bombas:
                                    hora_termino = datetime.now()
                                    diferenca_tempo = hora_termino - hora_inicio
                                    tempo_em_segundos = int(round(diferenca_tempo.total_seconds()))
                                    print("PARABÉNS VOCÊ ENCONTROU TODAS AS BOMB1AS\n Tempo da partida em segundos:", tempo_em_segundos)
                                    partida_continua = False
                                                                      
                                    nome_jogador = input("Digite o nome do jogador: ")
                                    tempo_partida_segundos = tempo_em_segundos
                                    quantidade_bombas_encontradas = bandeiras  

                                    historico.append({
                                        'jogador': nome_jogador,
                                        'tempo': tempo_partida_segundos,
                                        'bombas_encontradas': quantidade_bombas_encontradas
                                        })
                                    with open('historico_partidas.json', 'w') as arquivo:
                                        json.dump(historico, arquivo)
                                    bandeiras = 0
                                    limpar_terminal()
                        else:
                            print("A célula já foi aberta ou marcada anteriormente. Tente novamente.")

                    else:
                        print("Coordenadas fora do limite do tabuleiro. Tente novamente.")
                    limpar_terminal()
                    
                    
                                
                #abrir celula
                elif escolha == "2":
                    linha = int(input("Digite o número da linha: "))
                    coluna = int(input("Digite o número da coluna: "))
                    partida_continua = abrir_celula(tabuleiro_minado, tabuleiro_usuario, linha, coluna)
                    if not partida_continua:
                        break
                    limpar_terminal()
                    

                #desmarcar celula
                elif escolha == "3":
                    # Lógica para desmarcar uma célula
                    linha = int(input("Digite o número da linha: "))
                    coluna = int(input("Digite o número da coluna: "))
                    if 0 <= linha < tabuleiro_usuario.linhas and 0 <= coluna < tabuleiro_usuario.colunas:
                        if tabuleiro_usuario.tabuleiro[linha][coluna] == "M":
                            # Marca a célula no Tabuleiro_usuario
                            tabuleiro_usuario.tabuleiro[linha][coluna] = "?"
                            if tabuleiro_minado.tabuleiro[linha][coluna] == "ó":
                                bandeiras = bandeiras - 1
                                print("bandeiras marcadas corretamente:")
                                print(bandeiras)
                            else:
                                print("numero de bombas atuais")
                                print(bandeiras)

                        else:
                            print("A célula já foi aberta ou ainda não foi marcada anteriormente. Tente novamente.")
                    else:
                        print("Coordenadas fora do limite do tabuleiro. Tente novamente.")

                    limpar_terminal()

                #encerrar jogo
                elif escolha == "4":
                    partida_continua = False
                    limpar_terminal()
                    break


                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
                    limpar_terminal()

def abrir_celula(tabuleiro_minado, tabuleiro_usuario, linha, coluna):
    if 0 <= linha < tabuleiro_usuario.linhas and 0 <= coluna < tabuleiro_usuario.colunas:
        if tabuleiro_usuario.tabuleiro[linha][coluna] == "?":
            if tabuleiro_minado.tabuleiro[linha][coluna] == "ó":
                print("Você encontrou uma bomba. O jogo terminou!")
                limpar_terminal()         
                return False
            else:
                # Abra a célula no Tabuleiro_usuario
                tabuleiro_usuario.tabuleiro[linha][coluna] = tabuleiro_minado.tabuleiro[linha][coluna]

                vizinhas = obter_vizinhas(tabuleiro_usuario, linha, coluna)
                for vizinha in vizinhas:
                    x, y = vizinha
                    if tabuleiro_usuario.tabuleiro[x][y] == "?" and tabuleiro_minado.tabuleiro[x][y] != "ó":
                        tabuleiro_usuario.tabuleiro[x][y] = tabuleiro_minado.tabuleiro[x][y]
                return True
        else:
            print("A célula já foi aberta ou marcada anteriormente. Tente novamente.")
    else:
        print("Coordenadas fora do limite do tabuleiro. Tente novamente.")
    return True


def obter_vizinhas(tabuleiro_usuario, linha, coluna):
    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    vizinhas = []
    for dx, dy in direcoes:
        x, y = linha + dx, coluna + dy
        if 0 <= x < tabuleiro_usuario.linhas and 0 <= y < tabuleiro_usuario.colunas:
            vizinhas.append((x, y))
    return vizinhas

def verhistorico(historico):
    if not historico:
        print("Nenhum histórico disponível.")
    else:
        print("Histórico das Partidas:")
        for partida in historico:
            print(f"Jogador: {partida['jogador']}")
            print(f"Tempo da Partida (segundos): {partida['tempo']}")
            print(f"Bombas Encontradas: {partida['bombas_encontradas']}")
            print("------------------------------")

    input("Pressione Enter para continuar...")


if __name__ == "__main__":
    jogo = Play()
    jogo.main()