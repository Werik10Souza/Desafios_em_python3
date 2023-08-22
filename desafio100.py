
#*Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA() e SOMAPAR(). A primeira vai sortear 5 números e vai colocá-los dentro da LISTA e a segunda FUNÇÃO vai mostrar a SOMA entre todos os valores PARES sorteados pela função ANTERIOR.

from random import randint

soma = 0
par = 0

numeros = []

def sorteia():
    valores = (randint(0,4), randint(0,4), randint(0,4), randint(0,4), randint(0,4))
    for v in valores:
        numeros.append(v)
    print(numeros)

sorteia()

def somapar():
    if (numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]) % 2 == 0:
        par = sum(numeros)
    print(par)
somapar()
