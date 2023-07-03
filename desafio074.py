
#*Crie um programa que vai gerar 'cinco números aleatórios' e colocar em uma 'tupla'.
#*Depois disso, mostra a 'listagem de números' gerados e também indique o 'menor' e o 'maior' valor que estão na tupla.

from random import randint

maior = 0
menor = 0

numeros_aleatorios = randint(0,4)

maior = numeros_aleatorios + 1
menor = numeros_aleatorios - 1

print('-'*20)
print('LISTA DE NÚMEROS SORTEADOS\n')
print()
print('-'*20)
print('='*20)
print('MAIOR: {}'.format(maior))
print('MENOR: {}'.format(menor))
print('='*20)