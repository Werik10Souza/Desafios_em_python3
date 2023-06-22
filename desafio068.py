
#*Faça um programa que jogue PAR ou IMPAR com o computador. Jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

lista = ['par', 'impar']

computador = (random.choice(lista))

print(computador)
print('\n')

contador = 0

while (computador != lista):

    jogador = str(input('Qual foi sorteado pelo computador, par ou ímpar, na sua opnião?: '))

    ganhou = jogador == computador
    perdeu = jogador != computador

    contador = contador + ganhou

    if(ganhou):
        print('VOCÊ GANHOU!')
    elif(perdeu):
        print('VOCÊ PERDEU! O computador escolheu {}'.format(computador))
        break
print('\nTOTAL DE VITÓRIAS CONSECUTIVAS: {}'.format(contador))
