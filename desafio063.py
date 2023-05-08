
#* Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#* EX:
#* 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

numero = int(input('Quantos elementos você quer ver?: '))
primeiro = 0
segundo = 1 
contador = 3
print(primeiro, segundo, end= ' ')
while contador <= numero:
    terceiro = primeiro + segundo
    print(terceiro, end= ' ')
    primeiro = segundo
    segundo = terceiro
    contador = contador + 1