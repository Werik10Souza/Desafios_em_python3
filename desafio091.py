
#*Crie um programa onde 4 JOGADORES joguem um DADO e tinham resultados ALEATÓRIOS. Grande esses resultados em um
#*DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('VALORES SORTEADOS')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('='*30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)