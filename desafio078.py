
#*Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#*No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas posições na lista.

numeros = []

for contador in range(0,5):
    numeros.append(int(input('Digite o valor: ')))
print('\n',numeros)
print('\nFoi digitado na posição {}, o número'.format(numeros.index(max(numeros))), end='')
print(' {}, o MAIOR valor inserido'.format(max(numeros)))
print('foi digitado na posição {}, o número'.format(numeros.index(min(numeros))), end='')
print(' {}, o MENOR valor inserido'.format(min(numeros)))
