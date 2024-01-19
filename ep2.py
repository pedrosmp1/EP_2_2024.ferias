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