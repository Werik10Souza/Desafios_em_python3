
#*Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA() e SOMAPAR(). A primeira vai sortear 5 números e vai colocá-los dentro da LISTA e a segunda FUNÇÃO vai mostrar a SOMA entre todos os valores PARES sorteados pela função ANTERIOR.

from random import randint

numeros = []

def sorteia():
    valores = (randint(0,4), randint(0,4), randint(0,4), randint(0,4), randint(0,4))
    for v in valores:
        numeros.append(v)
    print(numeros)

sorteia()
