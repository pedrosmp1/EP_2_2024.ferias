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