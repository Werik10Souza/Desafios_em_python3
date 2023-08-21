
#*Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles e o MAIOR.

from random import randint

lista = []

def maior():
    print('-='*30)
    print('Analisando os valores passados...')
    numero = randint(0,10)
    for x in range(numero):
        lista.append(x)
    print(f'{lista} foram informados {len(lista)} ao todo')
    print(f'O maior valor informado foi {max(lista)}')
    print('-='*30)

maior()
