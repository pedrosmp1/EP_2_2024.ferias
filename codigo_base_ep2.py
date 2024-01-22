import random
from ep2 import *
# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    valido=False
    while not valido:
        linha=int(input('linha?'))
        
        while linha not in range(0,10):
            print('Linha inválida!')
            linha=int(input('linha?'))
        coluna=int(input('coluna?'))
        while coluna not in range(0,10):
            print('Coluna inválida!')
            coluna=int(input('coluna?'))
        if tabuleiro_oponente[linha][coluna]=='X' or tabuleiro_oponente[linha][coluna]=='-':
            print('A posição linha X e coluna Y já foi informada anteriormente!')
        else:
            valido=True
        
        
    tabuleiro_oponente= faz_jogada(tabuleiro_oponente,linha,coluna)
   
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
    if afundados(frota_oponente,tabuleiro_oponente)==len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False
        break

    linhaop=random.randint(0,9)
    colunaop=random.randint(0,9)
    while tabuleiro_oponente[linhaop][colunaop]=='X' or tabuleiro_oponente[linhaop][colunaop]=='-':
        print('A posição linha X e coluna Y já foi informada anteriormente!')
        linhaop=random.randint(0,9)
        colunaop=random.randint(0,9)
    tabuleiro_jogador= faz_jogada(tabuleiro_jogador,linhaop,colunaop)
    if afundados(frota_jogador,tabuleiro_jogador)==len(frota_jogador):
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando=False
        break



    

