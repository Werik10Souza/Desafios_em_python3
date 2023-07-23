
#*Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores lidos pelo teclado.

#! |_|_|_|
#! |_|_|_|
#! |_|_|_|

#?No final, mostre a MATRIZ na tela, com a formatação correta

matriz = []
numeros = []

for valor in range(0,9):
    valor = int(input('Digite um número inteiro: '))
    if valor not in numeros:
        numeros.append(valor)
    matriz.append(numeros[:])
    numeros.clear()

print('\n')

print(sorted(matriz))
print('\n')

print('M A T R I Z')
print('='*20)
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('='*20)