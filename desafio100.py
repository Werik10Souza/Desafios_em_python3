
#*Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA() e SOMAPAR(). A primeira vai sortear 5 números e vai colocá-los dentro da LISTA e a segunda FUNÇÃO vai mostrar a SOMA entre todos os valores PARES sorteados pela função ANTERIOR.

from random import randint
from time import sleep

def sorteia(lista):
    for contador in range(0,5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
