import re

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

##### INÍCIO DO EXERCÍCIO #####

def calcula_assinatura(texto):

    ### Tamanho médio de PALAVRA - WAL
    li_sentencas = separa_sentencas(texto)
    qtd_sentencas = len(li_sentencas)

    li_frases = []
    for i in range(len(li_sentencas)):
        li_frases = li_frases + separa_frases(li_sentencas[i])

    li_palavras = []
    for i in range(len(li_frases)):
        li_palavras = li_palavras + separa_palavras(li_frases[i])

    qtd_palavras = len(li_palavras)

    qtd_car = 0
    for i in range(len(li_palavras)):
        qtd_car = qtd_car + len(li_palavras[i])

    # Calcula quantidade de caracteres:
    i = 0
    qtd_car = 0
    while i < qtd_palavras:
        qtd_car = qtd_car + len(li_palavras[i])
        i = i + 1
    # Calcula tamanho médio da palavras:
    wal = qtd_car / qtd_palavras

    ### Relação TYPE-TOKEN - TTR
    # Calcula número de palavras diferentes:
    palavras_diferentes = n_palavras_diferentes(li_palavras)
    # Calcula relação type-token:
    ttr = palavras_diferentes / qtd_palavras

    ### Calcula Razão Hapax Legomana - HLR
    # Calcula número de palavras únicas:
    palavras_unicas = n_palavras_unicas(li_palavras)
    # Calcula relação HLR:
    hlr = palavras_unicas / qtd_palavras

    ### Tamanho Médio da SENTENÇA - SAL
    # Calcula carcteres da Sentença:
    qtd_car_sentenca = 0
    i = 0
    while i < len(li_sentencas):
        qtd_car_sentenca = qtd_car_sentenca + len(li_sentencas[i])
        i = i +1
    # Calcula a relação SAL:
    sal = qtd_car_sentenca / qtd_sentencas

    ### Complexidade Média da SENTENÇA - SAC
    # Calcula quantidade de frases:
    i = 0
    li_frases = []
    while i < len(li_sentencas):
        li_frases = li_frases + separa_frases(li_sentencas[i])
        i = i + 1
    qtd_frases = len(li_frases)
    # Calcula relação SAC:
    sac = qtd_frases / qtd_sentencas

    ### Tamanho Médio da FRASE - PAL:
    # Calcula o número de caracteres da frase:
    i = 0
    qtd_car_frase = 0
    while i < len(li_frases):
        qtd_car_frase = qtd_car_frase + len(li_frases[i])
        i = i + 1
    # Calcula relação PAL:
    pal = qtd_car_frase / qtd_frases
    ass = [wal, ttr, hlr, sal, sac, pal]
    return ass

def compara_assinatura(as_a, as_b):
#### Calcula similaridade
# Calcula Módulo:
    soma_modulo = 0
    for i in range(len(as_b)):
        f = abs(as_a[i] - as_b[i])
        soma_modulo = soma_modulo + f
    # Calcula S ab:
    sab = soma_modulo / 6
    return sab