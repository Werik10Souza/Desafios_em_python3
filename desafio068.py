
#*Faça um programa que jogue PAR ou IMPAR com o computador. Jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#?OPÇÃO 01:

import random

lista = ['par', 'impar']

computador = (random.choice(lista))


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

#!-----------------------------------//--------------------------------//-----------------------

#?OPÇÃO 02:

from random import randint

contador = 0

while True:
    jogador = int(input("Digite 0[PAR] e 1[ÍMPAR]: "))

    sorteo = randint(0, 1)

    ganhou = jogador == sorteo

    if ganhou:
        print("GANHOU!")
    else:
        print("PERDEU! Era {}".format(sorteo))
        break

    contador = contador + 1

print("\n")
print("-------//-----")
print("0 -> PAR")
print("1 -> ÍMPAR")
print("-------//-----")
print("\n")
print("========//=========")
print("FIM DE JOGO!")
print("========//=========")
print("\n")
print("VITÓRIAS CONSECUTIVAS: {}".format(contador))
