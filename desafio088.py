
#*Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 A 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.

from random import randint
from time import sleep

lista = []
jogos = []   

print('-'*30)
print('     JOGA NA MEGA SENA')
print('-'*30)
print('\n')

quantidade = int(input('Quantos jogos você quer que eu sorteie?: '))
print('\n')

total = 1

while total <= quantidade:
    contador =  0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador = contador + 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1

print('='* 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
print('\n')

for indice, linha in enumerate(jogos):
    print(f'jogo {indice+1}: {linha}')
    sleep(2)
print('\n')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)