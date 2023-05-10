
#* Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#? t = termo
#* EX:
#* 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#  t1 + t2 = t3

numero = int(input('Quantos elementos você quer ver?: '))
t1 = 0
t2 = 1 
contador = 3
print(t1, t2, end= ' ')
while contador <= numero:
    t3 = t1 + t2
    print(t3, end= ' ')
    t1 = t2
    t2 = t3
    contador = contador + 1
