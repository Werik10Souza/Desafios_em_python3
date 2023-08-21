
#*Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles e o MAIOR.

from random import randint

def maior():
    print('-='*30)
    print('Analisando os valores passados...')
    numero = randint(0,15)
    for x in range(numero):
        print(f'{x}', end=' ')
    print('\n','-='*30)

maior()
