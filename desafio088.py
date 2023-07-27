
#*Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 A 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.

from random import randint

palpites = []
numeros = []

jogos = int(input('Quantos jogos serão gerados?: '))
print('\n')

for numero in range(0,6):
    numero = randint(1,60)
    if numero not in numeros:
        numeros.append(numero)
        palpites.append(numeros[:])
        numeros.clear()
print('='*60)
print('                     P A L P I T E S')
print('='*60)

print(palpites * jogos)
