
#*Crie um programa onde 4 JOGADORES joguem um DADO e tinham resultados ALEATÓRIOS. Grande esses resultados em um
#*DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.

from random import randint

dicionario = {}

lista = []

contador = 0

for numero in range(0,4):
    numero = randint(1,6)
    dicionario['sorteado'] = numero
    lista.append(dicionario.copy())
    contador = contador + 1

print(lista)
print('\n')

print('VALORES SORTEADOS:')

for contador, numero in enumerate(lista):

    print(f'O jogador{contador+1} tem ', end=' ')
    for valor in numero.values():
        print(valor)

print('Ranking dos jogadores:')
