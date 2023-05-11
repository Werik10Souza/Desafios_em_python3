
#* Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#* EX:
#* 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#  t1 + t2 = t3

numero = int(input('Digite quantos elementos quer que apareça: '))

termo1 = 0
termo2 = 1
contador = 3

print(termo1, termo2, end=' ')

while contador <= numero:
    termo3 = termo1 + termo2
    print(termo3, end=' ')
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1

print('FIM', end=' ')
