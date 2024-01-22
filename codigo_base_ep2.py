import random
random.seed(199)
# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!
def define_posicoes(dados):
    l=[]
    l.append([dados['linha'],dados['coluna']])
    tam=dados['tamanho']

    if dados['orientacao']=='vertical':
        for i in range(dados['linha']+1,tam+dados['linha']):
            l.append([i,dados['coluna']])
    else:
        for i in range(dados['coluna']+1,tam+dados['coluna']):
            l.append([dados['linha'],i])
    return l

def preenche_frota(dados,nome, frota):
    ln=define_posicoes(dados)
    nd={}
    nd['tipo']=nome
    nd['posicoes']=ln
    frota.append(nd)
    return frota


def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

def posiciona_frota(frota):
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for navio in frota:
        for coord in navio['posicoes']:
            grid[coord[0]][coord[1]]=1
    return grid


def afundados(frota,tabuleiro):
    soma=0
    for navio in frota:
        afundado=True
        for coord in navio['posicoes']:
            if tabuleiro[coord[0]][coord[1]]!='X':
                afundado=False
        if afundado:
            soma+=1
    return soma


def posicao_valida(dados,frota):
    pos_desejada=define_posicoes(dados)
    for coord1 in pos_desejada:
        if coord1[0]>9 or coord1[0]<-1 or coord1[1]>9 or coord1[1]<-1:
                return False
    for navio in frota:
        for coord in navio['posicoes']:
            if coord in pos_desejada:
                return False
    return True


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
# from pprint import pformat
# print(pformat(tabuleiro_oponente))
jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    

    # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
    
    # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
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
