
#*Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de DETALHES
#*DO APROVETAMENTO de cada jogador.

while True:

    nome = str(input('Nome do Jogador: '))
    quantidades_partidas = int(input(f'Quantas partidas {nome} jogou?: '))

    contador = 0
    total = 0

    lista_gols = []

    while contador < quantidades_partidas:
        gols_partida = int(input(f'Quantos gols na partida{contador}?: '))
        lista_gols.append(gols_partida)
        contador = contador + 1
        total = total + gols_partida

    analise = {'Nome' : nome,
            'Gols' : lista_gols,
            'Total' : total}
    
    while True:
        resposta = str(input('\nQuer continuar[S/N]? ')).upper() [0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
        if resposta == 'N':
            break
