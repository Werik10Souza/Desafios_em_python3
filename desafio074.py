
#*Crie um programa que vai gerar 'cinco números aleatórios' e colocar em uma 'tupla'.
#*Depois disso, mostra a 'listagem de números' gerados e também indique o 'menor' e o 'maior' valor que estão na tupla.

from random import randint

numeros_aleat01 = randint(0,9)
numeros_aleat02 = randint(0,9)
numeros_aleat03 = randint(0,9)
numeros_aleat04 =  randint(0,9)
numeros_aleat05 = randint(0,9)

tupla = (numeros_aleat01, numeros_aleat02, numeros_aleat03, numeros_aleat04, numeros_aleat05)

print(tupla)


print('\n')
print('='*20)
print('MAIOR: {}'.format(max(tupla)))
print('MENOR: {}'.format(min(tupla)))
print('='*20)
